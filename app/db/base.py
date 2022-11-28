# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.trainee import Trainee  # noqa
from app.models.course import Course  # noqa