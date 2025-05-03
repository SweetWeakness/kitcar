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
    return {"payment": 177.32}
