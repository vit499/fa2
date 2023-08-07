from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
import logging

from app import schemas, crud
from app.api.deps import get_db

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/update", response_model=schemas.Flat)
def create_item_for_user(
    user_id: int, item: schemas.FlatCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
