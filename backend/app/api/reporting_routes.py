# Reporting endpoints for analytics

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.component import Component
from app.models.gun import Gun
from app.models.inventory import Inventory
from app.models.lifecycle import Lifecycle
from app.repositories.inventory_repo import InventoryRepository

router = APIRouter(prefix="/reports")


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    total_guns = db.query(Gun).count()
    total_components = db.query(Component).count()
    total_inventory_records = db.query(Inventory).count()
    total_lifecycle_events = db.query(Lifecycle).count()
    total_quantity = InventoryRepository(db).get_total_quantity()

    return {
        "total_guns": total_guns,
        "total_components": total_components,
        "total_inventory_records": total_inventory_records,
        "total_lifecycle_events": total_lifecycle_events,
        "total_quantity_in_stock": total_quantity,
    }
