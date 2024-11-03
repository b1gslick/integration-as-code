from fastapi import FastAPI

from app.routers import router
from service import models
from service.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
