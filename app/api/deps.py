from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_trainee(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.Trainee:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.trainee.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_trainee(
    current_trainee: models.Trainee = Depends(get_current_trainee),
) -> models.Trainee:
    if not crud.trainee.is_active(current_trainee):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_trainee


def get_current_active_superuser(
    current_trainee: models.Trainee = Depends(get_current_trainee),
) -> models.Trainee:
    if not crud.trainee.is_superuser(current_trainee):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_trainee
