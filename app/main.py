# fastAPI
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import get_settings

# routers
from app.endpoints import main_router, tags_metadata


app_conf = get_settings()
# приложение
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(main_router)
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
