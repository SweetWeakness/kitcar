from fastapi import APIRouter, Query
from typing import List, Optional, Dict, Union
from pydantic import BaseModel
from fastapi.responses import FileResponse
import datetime

from app.utils import replies_db


class CreateReply(BaseModel):
    username: str
    email: str
    cartype: str
    text: str
    rating: int


router = APIRouter(prefix="/images", tags=["images"])


@router.get("/{file_name}")
def get_rental_filter_options(file_name: str):
    """
    Получение картинки с backend'а
    """
    return FileResponse(path="./data/" + str(file_name))


@router.get("/{fdir}/{file_name}")
def get_rental_filter_options(fdir: str, file_name: str):
    """
    Получение картинки с backend'а в конкретной директории
    """
    return FileResponse(path="./data/%s/%s" % (fdir, str(file_name)))
