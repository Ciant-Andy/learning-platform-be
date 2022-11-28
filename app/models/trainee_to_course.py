from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class TraineeToCourse(Base):
    __tablename__ = 'TraineeToCourse'
    trainee_id = Column('trainee_id', ForeignKey('trainee.id'), primary_key=True)
    course_id = Column('course_id', ForeignKey('course.id'), primary_key=True)
    blurb = Column(String, nullable=False)
    trainee = relationship("Trainee", back_populates="course")
    course = relationship("Course", back_populates="trainee")
    """
    To do
    trainee_name = association_proxy(target_collection='trainee', attr='name')
    course_name = association_proxy(target_collection='course', attr='name')
    """
