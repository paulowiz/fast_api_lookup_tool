from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select, func, select, column, case, literal_column
import os

db_host = os.environ.get('POSTGRES_HOST')
db_database = os.environ.get('POSTGRES_DATABASE')
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')

connection_string = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}/{db_database}"
sync_connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_database}"
engine = create_async_engine(connection_string, echo=False)
sync_engine = create_engine(sync_connection_string, pool_pre_ping=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)

Base = declarative_base()