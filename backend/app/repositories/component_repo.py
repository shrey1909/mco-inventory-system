# Database access layer for components

from sqlalchemy.orm import Session

from app.models.component import Component


class ComponentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Component).all()

    def get_by_id(self, component_id: int):
        return self.db.query(Component).filter(Component.id == component_id).first()

    def get_by_assembly(self, assembly_id: int):
        return (
            self.db.query(Component)
            .filter(Component.assembly_id == assembly_id)
            .all()
        )
