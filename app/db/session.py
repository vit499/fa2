from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# engine = create_engine(settings.DB_URI, pool_pre_ping=True)
engine = create_engine(settings.DB_URI, pool_size=40, max_overflow=0, pool_timeout=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
