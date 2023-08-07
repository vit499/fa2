from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app import models, schemas
import logging

logger = logging.getLogger(__name__)


def get_flats(db: Session, skip: int = 0, limit: int = 100):
    logger.info("crud get_flats")
    a = db.query(models.Flat).offset(skip).limit(limit).all()
    logger.info(f"a={len(a)}")
    return a 


def create_flat(db: Session, flat: schemas.FlatCreate):
    db_flat = models.Flat(**flat.dict())
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat

def del_flats(db: Session):
    logger.info("crud flats del")
    db.execute(text('DELETE FROM dots'))
    db.commit()
    db.execute(text('DELETE FROM rooms'))
    db.commit()
    db.execute(text('DELETE FROM flats'))
    db.commit()
    a = db.query(models.Flat).all()
    logger.info(f"a={len(a)}")
    return a 
