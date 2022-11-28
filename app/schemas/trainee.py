from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class TraineeBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class TraineeCreate(TraineeBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class TraineeUpdate(TraineeBase):
    password: Optional[str] = None


class TraineeInDBBase(TraineeBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Trainee(TraineeInDBBase):
    pass


# Additional properties stored in DB
class TraineeInDB(TraineeInDBBase):
    hashed_password: str
