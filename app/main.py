# fastAPI
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# routers
#from app.services.auth.endpoints import router as auth_router
from app.services.main_page.endpoints import router as main_page_router
from app.services.buy_car.endpoints import router as buy_car_router
from app.services.credit_leasing.endpoints import router as credit_router
from app.services.rent.endpoints import router as rent_router

from app.settings import get_settings


app = FastAPI()
app_conf = get_settings()

# сервисы
#app.include_router(auth_router)
app.include_router(main_page_router)
app.include_router(buy_car_router)
app.include_router(credit_router)
app.include_router(rent_router)

# доступы извне к сервисам
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app.main:app",
                reload=True,
                host=app_conf.app_host,
                port=app_conf.app_port)
