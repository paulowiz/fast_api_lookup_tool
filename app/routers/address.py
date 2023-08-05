import sys

sys.path.append("../..")

from typing import Optional
from fastapi import Depends, APIRouter
from database import async_session
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/address",
    tags=["Address"],
    responses={404: {"description": "Not found"}}
)

class Address(BaseModel):
    first_name: str
    last_name: Optional[str]


def get_db():
    db = async_session
    yield db


@router.get("")
async def read_current_user(db: Session = Depends(get_db)):
    return {'test': 'test'}
