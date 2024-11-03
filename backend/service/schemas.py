from pydantic import BaseModel
from sqlalchemy.types import TIMESTAMP


class LargeDataBase(BaseModel):
    id: int
    hash: str
    big_data: str

    class Config:
        orm_mode = True
