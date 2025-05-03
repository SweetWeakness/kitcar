from fastapi import APIRouter, Query
from typing import List, Optional, Dict, Union

from app.utils import cars_db, cars_db_sell, add_dict_values

router = APIRouter(prefix="/rent", tags=["rent"])


@router.get("/get_variables")
def get_rental_filter_options():
    """
    Получение списка допустимых параметров для фильтрации в блоке
    "Аренда автомобиля"
    """
    return {
        "available_types": [
            {"key": 1, "value": "Sedan", "amount": 5},
            {"key": 2, "value": "Coupe", "amount": 15}
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

        # для потенциальной сортировки
        price_to: int = None,
        place_from: int = None,
        date_from: str = None,
        time_from: str = None,
        place_to: int = None,
        date_to: str = None,
        time_to: str = None,
):
    """
    Получение списка машин с заданными фильтрами с пагинацией
    """
    filtered_cars = []
    for row in cars_db_sell:
        if additional_params:
            required = additional_params.split(",")
            flg = True
            for req in required:
                if req == "1":
                    if row["brand_id"] == 1:
                        flg = False
                elif req == "2":
                    if row["model_id"] != 2:
                        flg = False
                elif req == "3":
                    if row["model_id"] == 3:
                        flg = False
            if not flg:
                continue

        if capacity:
            row_seats = int(row["seats"][0])
            required = capacity.split(",")
            flg = False
            for req in required:
                if req == "1":
                    if row_seats == 2:
                        flg = True
                elif req == "2":
                    if row_seats == 4:
                        flg = True
                elif req == "3":
                    if row_seats == 6:
                        flg = True
                elif req == "4":
                    if row_seats >= 8:
                        flg = True
            if not flg:
                continue

        if car_type:
            required = car_type.split(",")
            flg = False
            for req in required:
                if req == "1":
                    if row["body_id"] == 1:
                        flg = True
                elif req == "2":
                    if row["body_id"] == 2:
                        flg = True
            if not flg:
                continue

        row["price"] /= 1000
        if row["old_price"]:
            row["old_price"] /= 1000
        filtered_cars.append(row)

    return add_dict_values(filtered_cars[:limit])
