from fastapi import APIRouter
from typing import List, Dict, Union

from app.services.buy_car.schemas.filter_cars import Car
from app.utils import (cars_db_sell, brands, models,
                       bodies, transmissions, engines,
                       drives, generations, add_dict_values)


router = APIRouter(prefix="/buy_car", tags=["buy_car"])


@router.get("/get_variables")
def get_variables():
    """
    Получение допустимых параметров для фильтрации по авто для покупки
    """
    return {
        "brand": [{"key": key, "value": val} for key, val in brands.items()],
        "model": [{"key": key, "value": val} for key, val in models.items()],
        "generation": generations,
        "body": [{"key": key, "value": val} for key, val in bodies.items()],
        "transmission": [{"key": key, "value": val} for key, val in transmissions.items()],
        "engine": [{"key": key, "value": val} for key, val in engines.items()],
        "drive": [{"key": key, "value": val} for key, val in drives.items()],
        "volume_from": [1.0, 1.2, 1.5, 2.0, 3.0],
        "volume_to": [2.0, 2.5, 3.5, 5.0, 6.0],
        "year_from": list(range(2000, 2025)),
        "year_to": list(range(2000, 2025))
    }
# todo выше нужно понять че делать с generation - Шо за поколение авто, как хранить че имели ввиду под ним крч


@router.get("/get_cars")
def get_cars(
    brand: int = None,
    model: int = None,
    generation: str = None,
    body: int = None,
    transmission: int = None,
    engine: int = None,
    drive: int = None,
    volume_from: float = None,
    volume_to: float = None,
    year_from: int = None,
    year_to: int = None,
    mileage_from: float = None,
    mileage_to: float = None,
    price_from: float = None,
    price_to: float = None,
    limit: int = 12,
):
    """
    Получение машин для покупки после фильтрации
    """
    filtered_cars = []
    for row in cars_db_sell:
        if brand is not None and row["brand_id"] != brand:
            continue
        if model is not None and row["model_id"] != model:
            continue
        if generation is not None and row["generation"] != generation:
            continue
        if body is not None and row["body_id"] != body:
            continue
        if transmission is not None and row["transmission_id"] != transmission:
            continue
        if engine is not None and row["engine_id"] != engine:
            continue
        if drive is not None and row["drive_id"] != drive:
            continue

        if volume_from is not None and row["volume"] < volume_from:
            continue
        if volume_to is not None and row["volume"] > volume_to:
            continue
        if year_from is not None and row["year"] < year_from:
            continue
        if year_to is not None and row["year"] > year_to:
            continue
        if mileage_from is not None and row["mileage"] < mileage_from:
            continue
        if mileage_to is not None and row["mileage"] > mileage_to:
            continue
        if price_from is not None and row["price"] < price_from:
            continue
        if price_to is not None and row["price"] > price_to:
            continue

        filtered_cars.append(row)

    return add_dict_values(filtered_cars[:limit])
