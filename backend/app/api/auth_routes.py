# Authentication endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.database.session import get_db
from app.repositories.user_repo import UserRepository
from app.schemas.user_schema import UserSchema

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(credentials: UserSchema, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_by_username(credentials.username)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
