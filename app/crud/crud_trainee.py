from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.trainee import Trainee
from app.schemas.trainee import TraineeCreate, TraineeUpdate


class CRUDTrainee(CRUDBase[Trainee, TraineeCreate, TraineeUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Trainee]:
        return db.query(Trainee).filter(Trainee.email == email).first()

    def create(self, db: Session, *, obj_in: TraineeCreate) -> Trainee:
        db_obj = Trainee(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Trainee, obj_in: Union[TraineeUpdate, Dict[str, Any]]
    ) -> Trainee:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[Trainee]:
        trainee = self.get_by_email(db, email=email)
        if not trainee:
            return None
        if not verify_password(password, trainee.hashed_password):
            return None
        return trainee

    def is_active(self, trainee: Trainee) -> bool:
        return trainee.is_active

    def is_superuser(self, trainee: Trainee) -> bool:
        return trainee.is_superuser


trainee = CRUDTrainee(Trainee)
