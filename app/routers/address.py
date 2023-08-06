import sys

sys.path.append("..")

from typing import Optional
from fastapi import Depends, APIRouter
from database import async_session, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app import models

router = APIRouter(
    prefix="/address",
    tags=["Address"],
    responses={404: {"description": "Not found"}}
)


class Address(BaseModel):
    first_name: str
    last_name: Optional[str]


def get_db():
    db = SessionLocal()
    yield db


@router.get("/{text}")
async def read_all_by_text(query: str = 'RONDA', page_num: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
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
    response = {
        "total": data_length,
        "page_size": page_size,
        "total_pages": round(data_length / page_size),
        "current_page": page_num,
        "data": data[start:end],
    }
    return response
