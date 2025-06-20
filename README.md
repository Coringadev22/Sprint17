# 🧠 Projeto de Previsão de Rotatividade de Clientes (Churn Prediction)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![CatBoost](https://img.shields.io/badge/CatBoost-0.9336_AUC-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success.svg)

## 📍 Visão Geral

Este projeto foi desenvolvido para a **Interconnect**, uma operadora de comunicações, com o objetivo de criar um sistema preditivo capaz de identificar clientes propensos ao cancelamento de contrato (churn). A detecção antecipada permite que a empresa tome ações preventivas de retenção, como ofertas promocionais e condições especiais.

### 🎯 Objetivo Principal

Construir um modelo de Machine Learning que atinja **AUC-ROC ≥ 0.88** na previsão de churn, permitindo a identificação precoce de clientes em risco de cancelamento.

### 🏆 Resultado Alcançado

- **AUC-ROC: 0.9336** ✅ (Meta: ≥ 0.88)
- **Acurácia: 88.50%**
- **Recall (Churn): 79%**
- **F1-score (Churn): 78%**

## 📊 Estrutura do Projeto

```
Sprint17/
│
└── final_provider/
    ├── sprint17.ipynb          # Notebook principal com toda análise
    ├── contract.csv            # Dados contratuais dos clientes
    ├── personal.csv            # Dados pessoais e demográficos
    ├── internet.csv            # Serviços de internet
    ├── phone.csv               # Serviços de telefonia
    └── catboost_info/          # Logs de treinamento do CatBoost
```

## 🧰 Tecnologias Utilizadas

### Bibliotecas Principais
- **Pandas & NumPy**: Manipulação e análise de dados
- **Matplotlib & Seaborn**: Visualização de dados
- **Scikit-learn**: Pré-processamento e pipelines
- **CatBoost**: Modelo principal (melhor performance)
- **XGBoost**: Modelo alternativo testado
- **SHAP**: Explicabilidade do modelo

### Modelos Testados
1. **Logistic Regression** (Baseline)
2. **Random Forest**
3. **XGBoost**
4. **CatBoost** ✅ (Modelo vencedor)

## 📈 Metodologia

### 1. Análise Exploratória (EDA)
- Unificação de 4 conjuntos de dados através de `customerID`
- Análise de distribuições e correlações
- Identificação de padrões de churn por categoria

### 2. Engenharia de Features
Criação de variáveis derivadas que aumentaram significativamente a performance:

| Feature | Descrição |
|---------|-----------|
| `ContractDuration` | Tempo de permanência do cliente (em dias) |
| `AutoPay` | Identifica uso de pagamento automático |
| `ServiceCount` | Número total de serviços contratados |
| `AvgServiceCost` | Custo médio por serviço ativo |

### 3. Pré-processamento
- **Pipeline robusto** com `ColumnTransformer`
- Tratamento de valores ausentes
- Codificação de variáveis categóricas (`OneHotEncoder`)
- Normalização de variáveis numéricas (`StandardScaler`)

### 4. Modelagem
- Divisão estratificada (80/20)
- Ajuste de `scale_pos_weight` para lidar com desbalanceamento
- Validação cruzada para métricas robustas

### 5. Interpretabilidade
- Análise SHAP para entender fatores de decisão
- Identificação das features mais importantes

## 🔍 Principais Insights

### Fatores de Maior Risco de Churn:
1. **Baixo valor total acumulado** (`TotalCharges`)
2. **Contratos recentes** (menor `ContractDuration`)
3. **Mensalidades altas** (`MonthlyCharges`)
4. **Contrato mensal** (vs. anual/bianual)
5. **Pagamento via cheque eletrônico**
6. **Ausência de serviços de suporte**

### Perfil do Cliente com Alto Risco:
- Cliente novo (< 6 meses)
- Contrato month-to-month
- Sem serviços adicionais
- Pagamento não automático
- Mensalidade acima da média

## 💡 Recomendações de Negócio

1. **Programa de Fidelização Inicial**
   - Focar em clientes nos primeiros 6 meses
   - Oferecer descontos para migração para contratos anuais

2. **Incentivo ao Pagamento Automático**
   - Desconto para quem aderir ao débito automático
   - Campanhas educativas sobre conveniência

3. **Pacotes de Serviços**
   - Bundling com desconto progressivo
   - Destaque para segurança online e suporte técnico

4. **Monitoramento Proativo**
   - Dashboard com score de risco em tempo real
   - Alertas automáticos para equipe de retenção

## 🚀 Como Executar

### Pré-requisitos
```bash
Python 3.8+
Jupyter Notebook
```

### Instalação de Dependências
```bash
pip install pandas numpy matplotlib seaborn
pip install scikit-learn xgboost catboost shap
```

### Execução
1. Clone o repositório
2. Navegue até a pasta do projeto
3. Abra o Jupyter Notebook:
```bash
jupyter notebook sprint17.ipynb
```
4. Execute as células sequencialmente

## 📊 Estrutura dos Dados

### contract.csv
- `customerID`: Identificador único
- `BeginDate`: Data de início do contrato
- `EndDate`: Data de término (ou "No" se ativo)
- `Type`: Tipo de contrato (Month-to-month, One year, Two year)
- `PaymentMethod`: Método de pagamento
- `MonthlyCharges`: Valor mensal
- `TotalCharges`: Valor total pago

### personal.csv
- `gender`: Gênero do cliente
- `SeniorCitizen`: Indicador de idoso (0/1)
- `Partner`: Tem cônjuge (Yes/No)
- `Dependents`: Tem dependentes (Yes/No)

### internet.csv
- `InternetService`: Tipo de internet (DSL, Fiber optic, No)
- Serviços adicionais: OnlineSecurity, OnlineBackup, etc.

### phone.csv
- `MultipleLines`: Múltiplas linhas telefônicas (Yes/No)

## 📧 Contato

**Autor:** Lucas Coelho  
**Função:** Data Scientist  
**Email:** lukaslopes.coelho@icloud.com  
**Data:** 15 de Junho de 2025

---

## 📄 Licença

Este projeto foi desenvolvido como parte do Sprint 17 da TripleTen e está sujeito aos termos de uso acadêmico.

---

*"Transformando dados em insights acionáveis para reduzir churn e maximizar a retenção de clientes."* 