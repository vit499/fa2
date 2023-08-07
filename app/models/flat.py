from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from .database import Base
from app.db.base_class import Base


class Flat(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True, index=True)
    param1 = Column(String)
    param2 = Column(String)
    param3 = Column(String)

    rooms = relationship("Room", back_populates="owner")


