# Database access layer for inventory

from sqlalchemy.orm import Session

from app.models.inventory import Inventory


class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Inventory).all()

    def get_by_component(self, component_id: int):
        return (
            self.db.query(Inventory)
            .filter(Inventory.component_id == component_id)
            .first()
        )

    def get_total_quantity(self) -> int:
        from sqlalchemy import func

        result = self.db.query(func.sum(Inventory.quantity)).scalar()
        return result if result is not None else 0
