from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

db_host = 'localhost'
db_database = 'postgres'
db_user = 'test'
db_password = 'test'

connection_string = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}/{db_database}"
sync_connection_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_database}"
engine = create_async_engine(connection_string, echo=False)
sync_engine = create_engine(sync_connection_string, pool_pre_ping=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)