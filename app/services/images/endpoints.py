from fastapi import APIRouter, UploadFile, File
import shutil
import os
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uuid

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


@router.post("/upload_image")
async def upload_file(file: UploadFile = File(...)):
    """
    Загрузка файла на сервер в папку /uploads
    """
    ext = os.path.splitext(file.filename)[-1]  # сохраняем расширение
    unique_name = f"{uuid.uuid4()}{ext}"
    file_location = os.path.join(os.getcwd(), "data", "temp", unique_name)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"location": f"/images/temp/{unique_name}"}
