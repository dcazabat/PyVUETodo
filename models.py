from datetime import datetime
import app
from dataclasses import dataclass


@dataclass
class Task(app.db.model):

    id: int
    title: str
    date: datetime
    completed: bool = False

    id          = app.db.Colum(app.db.Integer(), primary_key=True)
    title       = app.db.Colum(app.db.String(140))
    date        = app.db.Colum(app.db.Datetime(), default=datetime.now())
    completed   = app.db.Colum(app.db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'Task {self.id} - {self.title}'