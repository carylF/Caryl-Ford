import wtforms
from wtforms import validators
from models.instructor import Instructor


class InstructorForm(wtforms.Form):

  name = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  faculty = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  department = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  id_num = wtforms.StringField(validators=[
      validators.Required(),
      validators.Length(max=30)])

  def validate_name(self, field):
      field.data = field.data.strip()

  def validate_faculty(self, field):
      field.data = field.data.strip()

  def validate_department(self, field):
      field.data = field.data.strip()

  def validate_id_num(self, field):
      field.data = field.data.strip()