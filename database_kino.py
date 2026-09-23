from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Данные для подключения к новой базе
DB_HOST = '217.71.129.139'
DB_PORT = 6347
DB_USER = 'Sudeeneess'
DB_PASS = 'zytgjvygfhjkm'
DB_NAME = 'kino_orm'

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass