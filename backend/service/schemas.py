from pydantic import UUID4, BaseModel


class LargeDataBase(BaseModel):
    id: UUID4 | None = None
    hash: str | None = None
    big_data: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
