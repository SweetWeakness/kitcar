from fastapi import APIRouter

from .subsections.tires.endpoints import router as tires_router

from app.utils import offers_bd


router = APIRouter(prefix="/parts", tags=["parts"])
router.include_router(tires_router)


@router.get("/offers")
def get_super_offers(limit: int = 4):
    """
    Получение рекомендаций с пагинацией по limit
    """
    return offers_bd[:limit]
