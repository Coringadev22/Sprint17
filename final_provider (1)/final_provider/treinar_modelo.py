# treinar_modelo.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
import joblib
from sklearn.compose import ColumnTransformer
import os
from pathlib import Path

# Definir diretórios
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
MODELS_DIR = BASE_DIR / 'models'

# Criar diretórios se não existirem
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

def load_data():
    """Carrega os dados dos arquivos CSV."""
    contract = pd.read_csv(DATA_DIR / 'contract.csv')
    personal = pd.read_csv(DATA_DIR / 'personal.csv')
    internet = pd.read_csv(DATA_DIR / 'internet.csv')
    phone = pd.read_csv(DATA_DIR / 'phone.csv')
    return contract, personal, internet, phone

def merge_data(contract, personal, internet, phone):
    """Combina os diferentes conjuntos de dados."""
    df = contract.merge(personal, on='customerID', how='left')
    df = df.merge(internet, on='customerID', how='left')
    df = df.merge(phone, on='customerID', how='left')
    return df

def prepare_data(df):
    """Prepara os dados para treinamento."""
    # Criar variável target
    df['churn'] = df['EndDate'].apply(lambda x: 0 if x == 'No' else 1)
    
    # Remover colunas irrelevantes
    df = df.drop(columns=['customerID', 'EndDate'])
    df = df.dropna(axis=0, how='any')
    
    # Separar features e target
    X = df.drop(columns=['churn'])
    y = df['churn']
    
    return X, y

def create_pipeline(X):
    """Cria o pipeline de pré-processamento e modelo."""
    # Separar colunas categóricas e numéricas
    cat_cols = X.select_dtypes(include=['object', 'bool']).columns.tolist()
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Pré-processadores
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    # Preprocessador completo
    preprocessor = ColumnTransformer([
        ('cat', cat_pipeline, cat_cols),
        ('num', num_pipeline, num_cols)
    ])
    
    # Pipeline final
    return Pipeline([
        ('preprocessor', preprocessor),
        ('model', DecisionTreeClassifier(max_depth=5, random_state=42))
    ])

def main():
    """Função principal de treinamento."""
    # Carregar e preparar dados
    print("Carregando dados...")
    contract, personal, internet, phone = load_data()
    
    print("Combinando datasets...")
    df = merge_data(contract, personal, internet, phone)
    
    print("Preparando dados para treinamento...")
    X, y = prepare_data(df)
    
    # Criar e treinar pipeline
    print("Criando e treinando modelo...")
    pipeline = create_pipeline(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.2, random_state=42
    )
    
    pipeline.fit(X_train, y_train)
    
    # Avaliar modelo
    print("Avaliando modelo...")
    y_pred_proba = pipeline.predict_proba(X_test)[:,1]
    roc_score = roc_auc_score(y_test, y_pred_proba)
    print(f'AUC-ROC: {roc_score:.4f}')
    
    # Salvar modelo
    print("Salvando modelo...")
    model_path = MODELS_DIR / 'modelo_churn.pkl'
    joblib.dump(pipeline, model_path)
    print(f"Modelo salvo em: {model_path}")

if __name__ == "__main__":
    main()
