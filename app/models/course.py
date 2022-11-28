from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .trainee_to_course import TraineeToCourse
from app.db.base_class import Base


class Course(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    trainee = relationship("TraineeToCourse", back_populates="course")