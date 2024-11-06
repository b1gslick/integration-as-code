from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import settings

url_object = URL.create(
    drivername=settings.db_drivername,
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_host,
    database=settings.db_name,
    port=settings.db_port,
)
engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
