from fastapi import APIRouter, Query
from typing import List, Optional, Dict, Union

from app.utils import cars_db

router = APIRouter(prefix="/rent", tags=["rent"])


@router.get("/get_variables")
def get_rental_filter_options():
    return {
        "available_types": [
            {"key": 1, "value": "Седан", "amount": 5},
            {"key": 2, "value": "Грузовик", "amount": 15}
        ],
        "available_capacity": [
            {"key": 1, "value": "2 человека", "amount": 25},
            {"key": 2, "value": "4 человека", "amount": 35},
            {"key": 3, "value": "6 человека", "amount": 45},
            {"key": 4, "value": "8 или больше", "amount": 55},
        ],
        "additional_params": [
            {"key": 1, "value": "Страховка", "amount": 65},
            {"key": 2, "value": "Детское кресло", "amount": 75},
            {"key": 3, "value": "GPS", "amount": 85},
        ],
        "available_places": [
            {"key": 1, "value": "Москва"},
            {"key": 2, "value": "Челябинск"},
        ]
    }


@router.get("/get_cars")
def get_rental_cars(
        limit: int,
        car_type: str = None,
        capacity: str = None,
        additional_params: str = None,
        place_from: int = None,
        date_from: str = None,
        time_from: str = None,
        place_to: int = None,
        date_to: str = None,
        time_to: str = None,
):
    return cars_db[:limit]
