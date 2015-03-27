from google.appengine.ext import db

from models.instructor import Instructor
from models.assistant import Assistant


class Activity(db.Model):
  activity_id = db.StringProperty(default=None)
  course_code = db.StringProperty(default=None)
  activity_type = db.StringProperty(default=False)
  day = db.StringProperty(default=None)
  time = db.StringProperty(default=None)
  instructor = db.ReferenceProperty(Instructor)
  assistant = db.ReferenceProperty(Assistant)
  room = db.StringProperty(default=None)


  @classmethod
  def get_by_activity_id(cls, activity_id):
    return cls.all().filter('activity_id=', activity_id).get()

  @classmethod
  def get_by_course_code(cls, course_code):
    return cls.all().filter('course_code=', course_code).get()

  @classmethod
  def get_by_type(cls, activity_type):
    return cls.all().filter('activity_type=', activity_type).get()

  def get_by_instructor(self, instructor):
    return self.instructor

  @classmethod
  def get_by_room(cls, room):
    return cls.all().filter('room=', room).get()
