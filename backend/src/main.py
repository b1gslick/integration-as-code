from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import router
from service import models
from service.database import engine


def create_app() -> FastAPI:
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(router)

    origins = [
        "http://localhost:3000",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
