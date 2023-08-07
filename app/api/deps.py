
from typing import Generator
import logging

from app.db.session import SessionLocal

logger = logging.getLogger(__name__)

def get_db() -> Generator:
    logger.info("get_db")
    try:
        db = SessionLocal()
        yield db
    finally:
        logger.info("db close")
        db.close()


