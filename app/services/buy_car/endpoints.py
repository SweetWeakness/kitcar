from fastapi import APIRouter
from typing import List, Dict, Union

from app.services.buy_car.schemas.filter_cars import Car
from app.utils import cars_db


router = APIRouter(prefix="/buy_car", tags=["buy_car"])


@router.get("/get_variables", response_model=Dict[str, Union[List[Dict[str, Union[int, str]]], List[Union[int, float, str]]]])
def get_variables():
    return {
         "brand": [
            {"key": 1, "value": "Koenigsegg"},
            {"key": 2, "value": "Nissan"},
            {"key": 3, "value": "Rolls-Royce"},
            {"key": 4, "value": "Toyota"},
            {"key": 5, "value": "BMW"},
            {"key": 6, "value": "Audi"},
            {"key": 7, "value": "Tesla"},
        ],
        "model": [
            {"key": 1, "value": "GT-R"},
            {"key": 2, "value": "Phantom"},
            {"key": 3, "value": "Corolla"},
            {"key": 4, "value": "X5"},
            {"key": 5, "value": "A4"},
            {"key": 6, "value": "Model S"},
        ],
        "generation": ["2020+", "2015–2019", "2010–2014", "Before 2010"],
        "body": [
            {"key": 1, "value": "Sedan"},
            {"key": 2, "value": "SUV"},
            {"key": 3, "value": "Coupe"},
            {"key": 4, "value": "Hatchback"},
            {"key": 5, "value": "Liftback"},
            {"key": 6, "value": "Crossover"},
            {"key": 7, "value": "Sport"},
            {"key": 8, "value": "Electric"},
            {"key": 9, "value": "Hybrid"},
        ],
        "transmission": [
            {"key": 1, "value": "Manual"},
            {"key": 2, "value": "Automatic"},
        ],
        "engine": [
            {"key": 1, "value": "Petrol"},
            {"key": 2, "value": "Diesel"},
            {"key": 3, "value": "Hybrid"},
            {"key": 4, "value": "Electric"},
        ],
        "drive": [
            {"key": 1, "value": "Front-Wheel Drive"},
            {"key": 2, "value": "Rear-Wheel Drive"},
            {"key": 3, "value": "All-Wheel Drive"},
        ],
        "volume_from": [1.0, 1.2, 1.5, 2.0, 3.0],
        "volume_to": [2.0, 2.5, 3.5, 5.0, 6.0],
        "year_from": list(range(2000, 2025)),
        "year_to": list(range(2000, 2025))
    }
# todo выше нужно понять че делать с generation - Шо за поколение авто, как хранить че имели ввиду под ним крч


@router.get("/get_cars", response_model=List[Car])
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
    return cars_db[:limit]
