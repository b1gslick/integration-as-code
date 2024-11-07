import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router
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


if __name__ == "__main__":
    logger = logging.getLogger("uvicorn.error")
    uvicorn.run(create_app(), log_level="trace")
