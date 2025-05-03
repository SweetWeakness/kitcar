from fastapi import APIRouter


from app.utils import tires_bd


router = APIRouter(prefix="/parts")


@router.get("/get_variables")
def get_variables():
    """
    Получение допустимых параметров для фильтрации по Шинам
    """
    return {
         "var1": [
            {"key": 1, "value": "Value # 1"},
            {"key": 2, "value": "Value # 2"},
            {"key": 3, "value": "Value # 3"},
        ],
        "var2": [
            {"key": 1, "value": "Value # 1"},
            {"key": 2, "value": "Value # 2"},
            {"key": 3, "value": "Value # 3"},
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
    filtered = []
    for row in tires_bd:
        if var1 and row.get("var1") != var1:
            continue
        if var2 and row.get("var2") != var2:
            continue
        filtered.append(row)
    return filtered[:limit]
