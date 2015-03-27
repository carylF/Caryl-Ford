import wtforms
from wtforms import validators
from models.activity import Activity


class ActivityForm(wtforms.Form):

  activity_id = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=10)])

  course_code = wtforms.StringField(validators=[
      validators.Required()])

  activity_type = wtforms.SelectField(validators=[
    validators.Required()],
    choices=[('Lab', 'Lab'), ('Lecture', 'Lecture'),
              ('Tutorial', 'Tutorial')])

  day = wtforms.SelectField(validators=[
    validators.Required()],
    choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
              ('Wednesday', 'Wednesday'), ('Thursday','Thursday'),
              ('Friday','Friday'), ('Saturday','Saturday')])

  time = wtforms.StringField(validators=[
      validators.Required()])

  room = wtforms.StringField(validators=[
      validators.Required()])

  def validate_activity_id(self, field):
      field.data = field.data.strip()

  def validate_course_code(self, field):
      field.data = field.data.strip()

  def validate_time(self, field):
      field.data = field.data.strip()

  def validate_room(self, field):
      field.data = field.data.strip()