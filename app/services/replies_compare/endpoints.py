from fastapi import APIRouter, Query
from typing import List, Optional, Dict, Union
from pydantic import BaseModel
import datetime

from app.utils import replies_db


class CreateReply(BaseModel):
    username: str
    email: str
    cartype: str
    text: str
    rating: int


router = APIRouter(prefix="/replies_compare", tags=["replies_compare"])


@router.get("/get_replies")
def get_rental_filter_options(limit: int = 4):
    """
    Получение списка с отзывами клиентов
    """
    return replies_db[:limit]


@router.get("/get_models")
def get_rental_filter_options():
    """
    Получение моделей авто для дальнейших сравнений в блоке "Отзывы и сравнения"
    """
    return list(map(lambda x: "Model #" + str(x), list(range(15))))


@router.post("/create_reply")
def get_rental_filter_options(new_reply: CreateReply):
    """
    Создание отзыва (все данные обязательны для ввода)
    """
    new_reply_d = new_reply.model_dump()

    new_reply_d["date"] = datetime.date.today()
    new_reply_d["id"] = 1
    new_reply_d["image_url"] = "/images/peugeot_3008.png"
    if "email" in new_reply_d:
        del new_reply_d["email"]

    replies_db.append(new_reply_d)
    return {"db updated": True}
