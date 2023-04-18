# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response

model_name = 'Best vs. Listed Truck Price'
version = "v1.0.0"

class Input(BaseModel):
    list_price: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "list_price": 20995.00
        }


class Output(BaseModel):
    prediction: str

@app.get('/info')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    """Return service health"""
    return {
        "ok"
    }


@app.post('/predict', response_model=Output)
async def model_predict(input: Input):
    """Predict with input"""
    response = get_model_response(input)
    return response
