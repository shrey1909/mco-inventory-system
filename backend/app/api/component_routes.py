# Component management endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.component_repo import ComponentRepository

router = APIRouter(prefix="/components")


@router.get("/")
def list_components(db: Session = Depends(get_db)):
    repo = ComponentRepository(db)
    return repo.get_all()


@router.get("/{component_id}")
def get_component(component_id: int, db: Session = Depends(get_db)):
    repo = ComponentRepository(db)
    component = repo.get_by_id(component_id)
    if not component:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Component {component_id} not found",
        )
    return component
