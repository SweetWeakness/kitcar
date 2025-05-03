from fastapi import APIRouter


from app.utils import offers_db


router = APIRouter(prefix="/tires")


@router.get("/get_variables")
def get_variables():
    """
    Получение допустимых параметров для фильтрации по Шинам
    """
    return {
         "var1": [
            {"key": 1, "value": "Koenigsegg"},
            {"key": 2, "value": "Nissan"},
            {"key": 3, "value": "Rolls-Royce"},
        ],
        "var2": [
            {"key": 1, "value": "GT-R"},
            {"key": 2, "value": "Phantom"},
            {"key": 3, "value": "Corolla"},
        ]
    }


@router.get("/get_tires")
def get_cars(
    var1: int = None,
    var2: int = None,
    limit: int = 12,
):
    """
    Получение списка шин после применения фильтрации
    """
    return offers_db[:limit]

