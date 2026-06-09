import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

POSTGRESQ_DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")

# 1. 비동기 전용 DB엔진 생성
engine = create_async_engine(
    POSTGRESQ_DATABASE_URL,
    echo=True
)

