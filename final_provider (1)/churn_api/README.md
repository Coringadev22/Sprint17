# API de Previsão de Churn

API FastAPI para fazer previsões de churn de clientes usando um modelo de machine learning treinado.

## Estrutura do Projeto

```
churn_api/
├── app/
│   ├── main.py                 # App FastAPI
│   │   ├── model/
│   │   │   ├── modelo_churn.pkl    # Modelo treinado
│   │   │   └── predictor.py        # Lógica de previsão
│   │   ├── schemas/
│   │   │   └── input_schema.py     # Esquema de entrada (validação com Pydantic)
│   │   ├── utils/
│   │   │   └── logger.py           # Logs de previsões
│   │   └── main.py
│   ├── requirements.txt
│   └── README.md
```

## Configuração

1. Crie um ambiente virtual Python:
```bash
python -m venv .venv
```

2. Ative o ambiente virtual:
```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.\.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Copie seu modelo treinado (`modelo_churn.pkl`) para a pasta `app/model/`

## Executando a API

1. Inicie o servidor:
```bash
uvicorn app.main:app --reload
```

2. Acesse a documentação da API:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /`: Página inicial
- `GET /health`: Verificação de saúde da API
- `POST /predict`: Fazer previsão de churn

### Exemplo de Requisição

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
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
         }'
```

## Logs

Os logs de previsão são salvos em:
- Console (stdout)
- Arquivo: `logs/predictions.log` 