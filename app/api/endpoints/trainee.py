from typing import List, Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from app.api import deps

from app import models, schemas, crud

router = APIRouter()

@router.get("", response_model=List[schemas.Trainee])
def get_trainees(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_trainee: models.Trainee = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve trainees.
    """
    trainees = crud.trainee.get_multi(db, skip=skip, limit=limit)
    return trainees


@router.put("/{trainee_id}", response_model=schemas.Trainee)
def update_trainee(
    *,
    db: Session = Depends(deps.get_db),
    trainee_id: int,
    trainee_in: schemas.TraineeUpdate,
    current_trainee: models.trainee = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a trainee.
    """
    trainee = crud.trainee.get(db, id=trainee_id)
    if not trainee:
        raise HTTPException(
            status_code=404,
            detail="The trainee with this name does not exist in the system",
        )
    trainee = crud.trainee.update(db, db_obj=trainee, obj_in=trainee_in)
    return trainee


@router.get("/{trainee_id}", response_model=schemas.Trainee)
def read_trainee_by_id(
    trainee_id: int,
    current_trainee: models.trainee = Depends(deps.get_current_active_trainee),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific trainee by id.
    """
    trainee = crud.trainee.get(db, id=trainee_id)
    if trainee == current_trainee:
        return trainee
    if not crud.trainee.is_superuser(current_trainee):
        raise HTTPException(
            status_code=400, detail="The trainee doesn't have enough privileges"
        )
    return trainee

