from pydantic import BaseModel, Field
from typing import Optional

class CustomerData(BaseModel):
    # Contract features
    Contract: str = Field(..., description="Tipo de contrato")
    PaperlessBilling: str = Field(..., description="Faturamento sem papel")
    PaymentMethod: str = Field(..., description="Método de pagamento")
    MonthlyCharges: float = Field(..., description="Cobranças mensais")
    TotalCharges: float = Field(..., description="Cobranças totais")
    
    # Personal features
    gender: str = Field(..., description="Gênero do cliente")
    SeniorCitizen: int = Field(..., description="Cliente idoso (0/1)")
    Partner: str = Field(..., description="Tem parceiro")
    Dependents: str = Field(..., description="Tem dependentes")
    
    # Internet features
    InternetService: str = Field(..., description="Tipo de serviço de internet")
    OnlineSecurity: str = Field(..., description="Segurança online")
    OnlineBackup: str = Field(..., description="Backup online")
    DeviceProtection: str = Field(..., description="Proteção de dispositivo")
    TechSupport: str = Field(..., description="Suporte técnico")
    StreamingTV: str = Field(..., description="Streaming de TV")
    StreamingMovies: str = Field(..., description="Streaming de filmes")
    
    # Phone features
    PhoneService: str = Field(..., description="Serviço de telefone")
    MultipleLines: str = Field(..., description="Múltiplas linhas")

    class ClientData(BaseModel):
        gender: str
        SeniorCitizen: int
        Partner: str
        Dependents: str
        tenure: int
        PhoneService: str
        MultipleLines: str
        InternetService: str
        OnlineSecurity: str
        OnlineBackup: str
        DeviceProtection: str
        TechSupport: str
        StreamingTV: str
        StreamingMovies: str
        Contract: str
        PaperlessBilling: str
        PaymentMethod: str
        MonthlyCharges: float
        TotalCharges: float