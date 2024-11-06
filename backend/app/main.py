import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router
from service import models
from service.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
logger = logging.getLogger("uvicorn.error")

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

if __name__ == "__main__":
    uvicorn.run(app, log_level="trace")
