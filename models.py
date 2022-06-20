from sqlalchemy import DATETIME, Boolean, Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

from datetime import datetime
from dataclasses import dataclass
from pathlib import Path

BASE_DIR=str(Path(__file__).parent.absolute())

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '/db.sqlite'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True)

Base = declarative_base()
@dataclass
class Task(Base):

    id: int
    title: str
    date: datetime
    completed: bool = False

    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(String(140))
    date = Column(DATETIME, default=datetime.now())
    completed = Column(Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"Task(id={self.id!r}, title={self.title!r}, date={self.date!r})"

Base.metadata.create_all(engine)