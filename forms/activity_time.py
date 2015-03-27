import wtforms
from wtforms import validators
from models.activity import Activity


class ActivityTimeForm(wtforms.Form):

  day = wtforms.SelectField(validators=[
    validators.Required()],
    choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
              ('Wednesday', 'Wednesday'), ('Thursday','Thursday'),
              ('Friday','Friday'), ('Saturday','Saturday')])

  time = wtforms.StringField(validators=[
      validators.Required()])

  def validate_time(self, field):
      field.data = field.data.strip()