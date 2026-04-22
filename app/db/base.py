from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models import Analysis, JobDescription, Resume, User  # noqa: E402, F401