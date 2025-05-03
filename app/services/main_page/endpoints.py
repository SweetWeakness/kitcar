from fastapi import APIRouter
from typing import List

from app.services.main_page.schemas.superoffers import CarOffer
from app.utils import cars_db_sell


router = APIRouter(prefix="/main_page", tags=["main_page"])


@router.get("/superoffers")
def get_super_offers(limit: int = 4):
    """
    Получение суперпредложений с пагинацией по limit
    """
    return cars_db_sell[:limit]
