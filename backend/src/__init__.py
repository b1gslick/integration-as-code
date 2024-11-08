import os

# from dotenv import load_dotenv

from src.settings import Settings

# load_dotenv()

settings = Settings(
    db_drivername=os.environ.get("db_drivername", "postgresql"),
    db_username=os.environ.get("db_username", ""),
    db_password=os.environ.get("db_password", ""),
    db_name=os.environ.get("db_name", ""),
    db_host=os.environ.get("db_host", ""),
    db_port=int(os.environ.get("db_port", 5435)),
    hash_service=os.environ.get("hash_service", ""),
)
