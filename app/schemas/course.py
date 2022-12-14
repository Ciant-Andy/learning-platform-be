from typing import Optional

from pydantic import BaseModel


# Shared properties
class CourseBase(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class CourseCreate(CourseBase):
    pass


# Properties to receive via API on update
class CourseUpdate(CourseBase):
    pass


class CourseInDBBase(CourseBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Course(CourseInDBBase):
    pass


# Additional properties stored in DB
class CourseInDB(CourseInDBBase):
    pass
