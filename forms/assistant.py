import wtforms
from wtforms import validators
from models.bus import Bus


class AssistantForm(wtforms.Form):

  name = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  faculty = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  department = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  status = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=10)])

  num_hours = wtforms.IntegerField(validators=[
      validators.Required()])

  qualifications = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=100)])

  def validate_name(self, field):
      field.data = field.data.strip()

  def validate_faculty(self, field):
      field.data = field.data.strip()

  def validate_department(self, field):
      field.data = field.data.strip()

  def validate_status(self, field):
      field.data = field.data.strip()

  def validate_qualifications(self, field):
      field.data = field.data.strip()