# Inventory endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.inventory_repo import InventoryRepository

router = APIRouter(prefix="/inventory")


@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    repo = InventoryRepository(db)
    return repo.get_all()


@router.get("/component/{component_id}")
def get_inventory_by_component(component_id: int, db: Session = Depends(get_db)):
    repo = InventoryRepository(db)
    record = repo.get_by_component(component_id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No inventory record found for component {component_id}",
        )
    return record
