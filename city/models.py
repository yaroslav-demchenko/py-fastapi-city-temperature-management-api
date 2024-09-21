from sqlalchemy.orm import relationship
from db.engine import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    additional_info = Column(String(512))

    temperatures = relationship("Temperature", back_populates="city")
