from ast import Param
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from .database import Base
from app.db.base_class import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    param1 = Column(String)
    param2 = Column(String)
    param3 = Column(String)
    owner_id = Column(Integer, ForeignKey("flats.id"))

    owner = relationship("Flat", back_populates="rooms")

    unitsubsubs = relationship("Dot", back_populates="owner")
