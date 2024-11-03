import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import Settings

load_dotenv()

db_settings = Settings(
    db_drivername=os.environ["db_drivername"],
    db_username=os.environ["db_username"],
    db_password=os.environ["db_password"],
    db_name=os.environ["db_name"],
    db_host=os.environ["db_host"],
    db_port=int(os.environ["db_port"]),
)

url_object = URL.create(
    drivername=db_settings.db_drivername,
    username=db_settings.db_username,
    password=db_settings.db_password,
    host=db_settings.db_host,
    database=db_settings.db_name,
    port=db_settings.db_port,
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
