import sys

sys.path.append("..")

from fastapi import Depends, APIRouter, HTTPException
from database import session
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import ReturnTypeFromArgs
from app import models


class UnAccent(ReturnTypeFromArgs):
    pass


router = APIRouter(
    prefix="/address",
    tags=["Address"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    db = session()
    yield db


@router.get("/{query}")
async def search_address_by_text(query: str = 'RoNdA', page_num: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    start = (page_num - 1) * page_size
    end = start + page_size
    data = db.query(models.Address) \
        .filter(
        models.Address.street.ilike(f"%{query}%") |
        models.Address.number.ilike(f"%{query}%") |
        models.Address.region.ilike(f"%{query}%") |
        models.Address.district.ilike(f"%{query}%") |
        models.Address.city.ilike(f"%{query}%") |
        models.Address.postcode.ilike(f"%{query}%") |
        models.Address.unit.ilike(f"%{query}%")
    ).all()
    data_length = len(data)
    if data_length % page_size != 0:
        total_pages = int((data_length / page_size)) + 1
    else:
        total_pages = round(data_length / page_size)

    if data_length == 0:
        response = {
            "total": data_length,
            "page_size": page_size,
            "total_pages": total_pages,
            "current_page": page_num,
            "data": data[start:end],
        }
        return response
    else:
        return HTTPException(status_code=404, detail="Address not found!")