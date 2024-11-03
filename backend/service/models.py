from sqlalchemy import TIMESTAMP, UUID, Column, Integer, String, text

from service.database import Base


class LargeData(Base):
    __tablename__ = "large_table"

    id = Column(Integer, primary_key=True, nullable=False)
    hash = Column(String, nullable=False)
    big_data = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
