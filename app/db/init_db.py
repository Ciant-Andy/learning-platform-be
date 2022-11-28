from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from db import base  # noqa: F401

def init_db(db: Session) -> None:

    trainee = crud.trainee.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not trainee:
        trainee_in = schemas.TraineeCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        trainee = crud.trainee.create(db, obj_in=trainee_in)  # noqa: F841
