from fastapi import APIRouter

# routers
#from app.services.auth.endpoints import router as auth_router
from app.services.main_page.endpoints import router as main_page_router
from app.services.buy_car.endpoints import router as buy_car_router
from app.services.credit_leasing.endpoints import router as credit_router
from app.services.rent.endpoints import router as rent_router
from app.services.parts.endpoints import router as parts_router
from app.services.replies_compare.endpoints import router as replies_router


main_router = APIRouter()

#app.include_router(auth_router)
main_router.include_router(main_page_router)
main_router.include_router(buy_car_router)
main_router.include_router(credit_router)
main_router.include_router(rent_router)
main_router.include_router(parts_router)
main_router.include_router(replies_router)


tags_metadata = [
    {
        "name": "main_page",
        "description": "Главная страница",
    },
    {
        "name": "buy_car",
        "description": "Купить авто",
    },
    {
        "name": "credit_leasing",
        "description": "Кредит и лизинг",
    },
    {
        "name": "rent",
        "description": "Снять авто",
    },
    {
        "name": "parts",
        "description": "Запчасти и шины",
    },
    {
        "name": "replies_compare",
        "description": "Отзывы и сравнения",
    }
]