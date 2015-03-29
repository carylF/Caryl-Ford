from forms.activity import ActivityForm
from forms.assign_assistant import AssignAssistantForm
from forms.activity_time import ActivityTimeForm
from handlers import base
from library import messages
from library import constants
from library.auth import role_required
from models.assistant import Assistant
from models.activity import Activity
from models.profile import Profile


class ActivityHandler(base.BaseHandler):

  @role_required(is_manager=True)
  def create(self):
    form = ActivityForm(self.request.POST)

    if self.request.method == 'POST' and form.validate():

      if Activity.get_by_activity_id(form.data['']):
        self.session.add_flash(messages.BUS_EXISTS,
                               level='error')
        return self.render_to_response('activity/form.haml', {'form': form})

      activity = Activity(activity_id=form.data['activity_id'],
                course_code=form.data['course_code'],
                activity_type=form.data['activity_type'],
                day=form.data['day'],
                time=form.data['time'],
                room=form.data['room'],
                parent=self.get_current_account())
      activity.put()

      self.session.add_flash(messages.BUS_CREATE_SUCCESS, level='info')
      return self.redirect_to('activity.list')

    self.session.add_flash(messages.BUS_CREATE_ERROR, level='error')
    return self.redirect_to('activity.list')

  @role_required(is_manager=True)
  def delete(self, id):
    activity = Activity.get_by_activity_id(int(id), parent=self.get_current_account())

    if not activity:
      self.session.add_flash(messages.BUS_NOT_FOUND, level='error')
      return self.redirect_to('activity.list')

    activity.delete()
    self.session.add_flash(messages.BUS_DELETE_SUCCESS)

    return self.redirect_to('activity.list')

  def list(self):
    # We pass form so we can generate it with the modal using macros.
    return self.render_to_response('activity/list.haml', {'form': ActivityForm()})

  @role_required(is_manager=True, is_editor=True)
  def update_times(self, id):
    activity = Activity.get_by_activity_id(int(id), parent=self.get_current_account())

    if not activity:
      return self.redirect_to('activity.list', messages.BUS_NOT_FOUND)

    form = ActivityTimeForm(self.request.POST, obj=activity)

    if self.request.method == 'POST' and form.validate():
      form.populate_obj(activity)
      activity.put()

      self.session.add_flash(messages.BUS_Times_SUCCESS)
      return self.redirect_to('activity.list')

    return self.render_to_response('activity/form.haml', {'form': form})


  @role_required(is_manager=True)
  def assign_assistant(self, id):
    activity = Activity.get_by_id(int(id), parent=self.get_current_account())

    if not activity:
      return self.redirect_to('activity.list', messages.BUS_NOT_FOUND)

    form = AssignAssistantForm(self.request.POST)

    if self.request.method == 'POST' and form.validate():

      assistant = Assistant.get_by_assistant_id(form.data['assistant_id'])

      if not assistant:
        return self.redirect_to('activity.list', messages.BUS_DRIVER_NOT_FOUND)

      activity.assistant = assistant
      activity.put()

      self.session.add_flash(messages.BUS_DRIVER_ASSIGN_SUCCESS)
      return self.redirect_to('activity.list')

    self.session.add_flash(messages.BUS_DRIVER_ASSIGN_ERROR, level='error')
    return self.redirect_to('activity.list')


  @role_required(is_manager=True, is_editor=True)
  def update(self, id):
    activity = Activity.get_by_id(int(id), parent=self.get_current_account())

    if not activity:
      return self.redirect_to('activity.list', messages.BUS_NOT_FOUND)

    form = ActivityForm(self.request.POST, obj=activity)

    if self.request.method == 'POST' and form.validate():
      form.populate_obj(activity)
      activity.put()

      self.session.add_flash(messages.BUS_UPDATE_SUCCESS)
      return self.redirect_to('activity.list')

    return self.render_to_response('activity/form.haml', {'form': form})