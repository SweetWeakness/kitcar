from fastapi import APIRouter, Form
from typing import List
from pydantic import BaseModel

class CalculatorResult(BaseModel):
    payment: float


router = APIRouter(prefix="/credit_leasing", tags=["credit_leasing"])


@router.get("/calculate", response_model=CalculatorResult)
def calculate_payment(amount: float, term_years: int, rate: float = 16.0):
    months = term_years * 12
    monthly_rate = rate / 100 / 12
    payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    return {"payment": round(payment)}
