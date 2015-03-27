from google.appengine.ext import db


class Assistant(db.Model):
  name = db.StringProperty(default=None)
  faculty = db.StringProperty(default=False)
  department = db.StringProperty(default=None)
  assistant_id = db.StringProperty(default=None)
  status = db.StringProperty(default=None)
  num_hours = db.IntegerProperty(default=None)
  qualifications = db.StringProperty(default=None)


  @classmethod
  def get_by_assistant_id(cls, id_num):
    return cls.all().filter('id_num=', id_num).get()

  @classmethod
  def get_by_faculty(cls, faculty):
    return cls.all().filter('faculty=', faculty).get()

  @classmethod
  def get_by_department(cls, department):
    return cls.all().filter('department=', department).get()