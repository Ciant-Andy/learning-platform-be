from typing import List, Any

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps

from app import models, schemas, crud

router = APIRouter()

@router.get("/", response_model=List[schemas.Course])
def get_all_course(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve courses.
    """
    course = crud.course.get_multi(db, skip=skip, limit=limit)
    return course

@router.post("/", response_model=schemas.Course)
def create_course(
    *,
    db: Session = Depends(deps.get_db),
    course_in: schemas.CourseCreate,
) -> Any:
    """
    Create new course.
    """
    course = crud.item.create_with_owner(db=db, obj_in=course_in)
    return course

@router.delete("/{id}", response_model=schemas.Course)
def delete_course(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an course.
    """
    course = crud.course.get(db=db, id=id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course = crud.course.remove(db=db, id=id)
    return course
