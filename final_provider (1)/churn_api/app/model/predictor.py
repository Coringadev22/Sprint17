import joblib
import pandas as pd
from pathlib import Path
from ..schemas.input_schema import CustomerData

class ChurnPredictor:
    def __init__(self, model_path: str = None):
        if model_path is None:
            # Usando caminho absoluto para o modelo
            current_dir = Path(__file__).resolve().parent
            model_path = current_dir.parent.parent.parent / "final_provider" / "models" / "modelo_churn.pkl"
            print(f"Loading model from: {model_path}")  # Debug print
        
        # Load the model
        try:
            print(f"Model path exists: {Path(model_path).exists()}")  # Debug print
            self.model = joblib.load(model_path)
            print("Model loaded successfully")  # Debug print
        except Exception as e:
            print(f"Error loading model: {str(e)}")  # Debug print
            raise RuntimeError(f"Error loading model: {str(e)}")
    
    def _preprocess_data(self, customer_data: CustomerData) -> pd.DataFrame:
        """
        Converte os dados do cliente em um DataFrame no formato esperado pelo modelo
        """
        # Convert to dictionary and then to DataFrame
        data_dict = customer_data.dict()  # Using dict() for Pydantic v1
        
        # Mapear Contract para Type
        if 'Contract' in data_dict:
            data_dict['Type'] = data_dict.pop('Contract')
        
        # Adicionar campos necessários com valores padrão
        data_dict['BeginDate'] = '2023-01-01'  # Data padrão
        data_dict['EndDate'] = 'No'  # Assumimos que o cliente ainda está ativo
        
        # Criar DataFrame com as colunas na ordem correta
        df = pd.DataFrame([data_dict])
        
        # Converter tipos de dados para corresponder ao treinamento
        numeric_cols = ['MonthlyCharges', 'TotalCharges']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)
        
        return df
    
    def predict(self, customer_data: CustomerData) -> float:
        """
        Faz a previsão de churn para um cliente
        """
        # Preprocess the data
        input_df = self._preprocess_data(customer_data)
        
        # Make prediction
        try:
            # O modelo é um pipeline que já inclui o pré-processamento
            prediction = self.model.predict_proba(input_df)[0][1]  # Probabilidade da classe positiva (churn)
            return float(prediction)  # Converter para float para garantir serialização JSON
        except Exception as e:
            print(f"Error in prediction: {str(e)}")  # Debug print
            raise RuntimeError(f"Error making prediction: {str(e)}")