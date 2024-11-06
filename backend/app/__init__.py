import os

from dotenv import load_dotenv

from app.settings import Settings

load_dotenv()

settings = Settings(
    db_drivername=os.environ["db_drivername"],
    db_username=os.environ["db_username"],
    db_password=os.environ["db_password"],
    db_name=os.environ["db_name"],
    db_host=os.environ["db_host"],
    db_port=int(os.environ["db_port"]),
    hash_service=os.environ.get("hash_service", ""),
)
