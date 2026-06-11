from pydantic import BaseModel, Field

class InsuranceCreate(BaseModel):
    smoker: int = Field(..., example=1)
    age: int = Field(..., example=25)
    bmi: float = Field(..., example=30.0)

class InsuranceResponse(BaseModel):
    id: int
    smoker: int = Field(..., example=0)
    age: int = Field(..., example=25)
    bmi: float = Field(..., example=30.0)
    charges: float = Field(..., example=1000.0)