import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.utils import calculate_hash
from service import models, schemas
from service.database import get_db

router = APIRouter(
    prefix="/large_data",
)


@router.get("/", response_model=list[schemas.LargeDataBase])
async def get_all_large_data(db: Session = Depends(get_db)):
    data = db.query(models.LargeData).all()

    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=str)
async def post_large_data(
    post_data: schemas.LargeDataBase, db: Session = Depends(get_db)
):
    _id = uuid.uuid4()

    hash = await calculate_hash(post_data.big_data)

    if hash is None:
        hash = ""

    new_data = models.LargeData(
        id=_id,
        hash=hash,
        big_data=post_data.big_data,
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return hash


@router.get(
    "/{id}", response_model=schemas.LargeDataBase, status_code=status.HTTP_200_OK
)
async def get_one_large_row(id: int, db: Session = Depends(get_db)):
    id_ld = db.query(models.LargeData).filter(models.LargeData.id == id).first()

    if id_ld is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id: {id} you requested for does not exist",
        )

    return id_ld


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_data_row(id: int, db: Session = Depends(get_db)):
    deleted = db.query(models.LargeData).filter(models.LargeData.id == id)

    if deleted.first() is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id: {id} you requested for does not exist",
        )
    deleted.delete(synchronize_session=False)
    db.commit()


@router.put("/large_data/{id}", response_model=schemas.LargeDataBase)
def update_large_data(
    updated: schemas.LargeDataBase, id: int, db: Session = Depends(get_db)
):
    old = db.query(models.LargeData).filter(models.LargeData.id == id)

    if old.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} does not exist"
        )
    updated_data = {
        column.name: getattr(updated, column.name)
        for column in models.LargeData._table_.columns
    }
    old.update(updated_data, synchronize_session=False)

    db.commit()

    return old.first()
