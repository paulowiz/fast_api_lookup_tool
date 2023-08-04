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


# models.Base.metadata.create_all(bind=engine)


class User(BaseModel):
    first_name: str
    last_name: Optional[str]


class Password(BaseModel):
    current_password: str
    new_password: str


def get_db():
    try:
        db = async_session()
        yield db
    finally:
        db.close()


@router.get("")
async def read_current_user(db: Session = Depends(get_db)):
    return {'test': 'test'}
