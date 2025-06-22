# 🎯 API de Previsão de Churn

API para prever a probabilidade de um cliente cancelar seus serviços (churn) com base em suas características e padrões de uso.

## 📊 Visão Geral

Este projeto implementa uma API REST que utiliza um modelo de machine learning para prever a probabilidade de churn de clientes. O modelo foi treinado com dados históricos de clientes e alcançou um score AUC-ROC de 0.8165.

## 🛠️ Tecnologias Utilizadas

- Python 3.10
- FastAPI
- scikit-learn
- pandas
- numpy
- uvicorn

## 📁 Estrutura do Projeto

```
.
├── churn_api/
│   ├── app/
│   │   ├── main.py           # Aplicação FastAPI
│   │   ├── model/
│   │   │   └── predictor.py  # Classe de predição
│   │   ├── schemas/
│   │   │   └── input_schema.py # Schemas Pydantic
│   │   └── utils/
│   │       └── logger.py     # Configuração de logs
│   └── venv310/             # Ambiente virtual
├── final_provider/
│   ├── data/               # Dados de treinamento
│   ├── models/            # Modelo treinado
│   └── treinar_modelo.py  # Script de treinamento
└── tests/                # Testes da API
```

## ⚙️ Configuração do Ambiente

1. Clone o repositório
2. Crie um ambiente virtual Python 3.10:
```bash
python -m venv venv310
```

3. Ative o ambiente virtual:
```bash
# Windows
.\venv310\Scripts\activate

# Linux/Mac
source venv310/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando a API

1. Ative o ambiente virtual (se ainda não estiver ativo)
2. Navegue até a pasta da API:
```bash
cd churn_api
```

3. Inicie o servidor:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

## 📝 Endpoints

### POST /predict

Faz uma previsão de churn para um cliente.

**Exemplo de requisição:**

```json
{
    "InternetService": "Fiber optic",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 79.85,
    "TotalCharges": 3320.75,
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "PhoneService": "Yes",
    "MultipleLines": "No"
}
```

**Exemplo de resposta:**

```json
{
    "churn_probability": 0.82
}
```

## 📊 Campos do Modelo

| Campo | Tipo | Descrição | Valores Possíveis |
|-------|------|-----------|-------------------|
| InternetService | string | Tipo de serviço de internet | "DSL", "Fiber optic", "No" |
| Contract | string | Tipo de contrato | "Month-to-month", "One year", "Two year" |
| PaperlessBilling | string | Faturamento sem papel | "Yes", "No" |
| PaymentMethod | string | Método de pagamento | "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)" |
| MonthlyCharges | float | Valor mensal cobrado | Número decimal |
| TotalCharges | float | Valor total cobrado | Número decimal |
| gender | string | Gênero do cliente | "Female", "Male" |
| SeniorCitizen | integer | Cliente idoso | 0 ou 1 |
| Partner | string | Cliente tem parceiro | "Yes", "No" |
| Dependents | string | Cliente tem dependentes | "Yes", "No" |
| OnlineSecurity | string | Tem segurança online | "Yes", "No", "No internet service" |
| OnlineBackup | string | Tem backup online | "Yes", "No", "No internet service" |
| DeviceProtection | string | Tem proteção de dispositivo | "Yes", "No", "No internet service" |
| TechSupport | string | Tem suporte técnico | "Yes", "No", "No internet service" |
| StreamingTV | string | Tem streaming de TV | "Yes", "No", "No internet service" |
| StreamingMovies | string | Tem streaming de filmes | "Yes", "No", "No internet service" |
| PhoneService | string | Tem serviço de telefone | "Yes", "No" |
| MultipleLines | string | Tem múltiplas linhas | "Yes", "No", "No phone service" |

## 🧪 Testes

Para executar os testes:

```bash
python -m pytest tests/
```

## 📈 Performance do Modelo

- AUC-ROC Score: 0.8165
- O modelo foi treinado usando Decision Tree com profundidade máxima de 5
- Features mais importantes incluem tipo de contrato, método de pagamento e serviços contratados 