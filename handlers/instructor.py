from forms.instructor import InstructorForm
from handlers import base
from library import messages
from library import constants
from library.auth import role_required
from models.instructor import Instructor
from models.profile import Profile


class InstructorHandler(base.BaseHandler):

  @role_required(is_manager=True)
  def create(self):
    form = InstructorForm(self.request.POST)

    if self.request.method == 'POST' and form.validate():

      if Instructor.get_by_instructor_id(form.data['id_num']):
        self.session.add_flash(messages.INSTRUCTOR_EXISTS,
                               level='error')
        return self.render_to_response('instructor/form.haml', {'form': form})

      instructor = Instructor(name=form.data['name'],
                            faculty=form.data['faculty'],
                            department=form.data['department'],
                            id_num=form.data['id_num'],
                            parent=self.get_current_account())
      instructor.put()

      self.session.add_flash(messages.INSTRUCTOR_CREATE_SUCCESS, level='info')
      return self.redirect_to('instructor.list')

    self.session.add_flash(messages.INSTRUCTOR_CREATE_ERROR, level='error')
    return self.redirect_to('instructor.list')

  @role_required(is_manager=True)
  def delete(self, id):
    instructor = Instructor.get_by_id(int(id), parent=self.get_current_account())

    if not instructor:
      self.session.add_flash(messages.INSTRUCTOR_NOT_FOUND, level='error')
      return self.redirect_to('instructor.list')

    instructor.delete()
    self.session.add_flash(messages.INSTRUCTOR_DELETE_SUCCESS)

    return self.redirect_to('instructor.list')

  @role_required(is_manager=True, is_editor=True)
  def update(self, id):
    instructor = Instructor.get_by_id(int(id), parent=self.get_current_account())

    if not instructor:
      return self.redirect_to('instructor.list', messages.INSTRUCTOR_NOT_FOUND)

    form = InstructorForm(self.request.POST, obj=instructor)

    if self.request.method == 'POST' and form.validate():
      form.populate_obj(instructor)
      # instructor.name = ' '.join((form.data['first_name'],
      #                             form.data['last_name']))
      instructor.put()

      self.session.add_flash(messages.INSTRUCTOR_UPDATE_SUCCESS)
      return self.redirect_to('instructor.list')

    return self.render_to_response('instructor/form.haml', {'form': form})

  def list(self):
    # We pass form so we can generate it with the modal using macros.
    return self.render_to_response('instructor/list.haml', {'form': InstructorForm()})
