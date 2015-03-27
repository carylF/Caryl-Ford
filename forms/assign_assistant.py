import wtforms
from wtforms import validators
from models.assistant import Assistant


class AssignAssistantForm(wtforms.Form):

  assistant_id = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=10)])

  def validate_driver_id(self, field):
      field.data = field.data.strip()