# Lifecycle tracking endpoints

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.lifecycle import Lifecycle

router = APIRouter(prefix="/lifecycle")


@router.get("/")
def track_lifecycle(db: Session = Depends(get_db)):
    records = db.query(Lifecycle).all()
    return records
