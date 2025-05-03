from fastapi import APIRouter, Form
from typing import List
from pydantic import BaseModel

class CalculatorResult(BaseModel):
    payment: float


router = APIRouter(prefix="/credit_leasing", tags=["credit_leasing"])


@router.get("/calculate", response_model=CalculatorResult)
def calculate_payment(amount: int, period: int, bank: int):
    """
    Вычисление ежемесячного платежа
    """
    payment = amount / 12 / period
    if bank == 1:
        payment *= 0.7
    elif bank == 2:
        payment *= 0.8
    elif bank == 3:
        payment *= 0.9
    return {"payment": round(payment)}
