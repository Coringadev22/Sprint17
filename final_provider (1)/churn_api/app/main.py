from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas.input_schema import CustomerData
from .model.predictor import ChurnPredictor
import logging

# Initialize FastAPI app
app = FastAPI(
    title="Churn Prediction API",
    description="API para prever a probabilidade de churn de clientes",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("churn_api")

# Initialize predictor
try:
    predictor = ChurnPredictor()
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    predictor = None

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Previsão de Churn"}

@app.get("/health")
async def health_check():
    if predictor is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy"}

@app.post("/predict")
async def predict_churn(customer_data: CustomerData):
    if predictor is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
        
    try:
        # Get prediction
        prediction = predictor.predict(customer_data)
        
        # Log prediction
        logger.info(f"Prediction made for customer data")
        
        return {
            "churn_probability": float(prediction),
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 