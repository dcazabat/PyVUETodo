from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired

class TaskForm(Form):
    title = StringField('title', validators=[DataRequired()])

