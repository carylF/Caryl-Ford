from forms.assistant import AssistantForm
from handlers import base
from library import messages
from library import constants
from library.auth import role_required
from models.assistant import Assistant
from models.profile import Profile


class AssistantHandler(base.BaseHandler):

  @role_required(is_manager=True)
  def create(self):l
    form = AssistantForm(self.request.POST)

    if self.request.method == 'POST' and form.validate():

      if Assistant.get_by_driver_id(form.data['driver_id']):
        self.session.add_flash(messages.BUS_DRIVER_EXISTS,
                               level='error')
        return self.render_to_response('assistant/form.haml', {'form': form})

      assistant = Assistant(assistant_id=form.data['assistant_id'],
                            facility=form.data['facility'],
                            department=form.data['department'],
                            status=form.data['status'],
                            num_hours=form.data['num_hours'],
                            qualifications=form.data['qualifications'],
                            parent=self.get_current_account())

      assistant.name = ' '.join((form.data['first_name'],
                                  form.data['last_name']))
      assistant.put()

      self.session.add_flash(messages.BUS_DRIVER_CREATE_SUCCESS, level='info')
      return self.redirect_to('assistant.list')

    self.session.add_flash(messages.BUS_DRIVER_CREATE_ERROR, level='error')
    return self.redirect_to('assistant.list')

  @role_required(is_manager=True)
  def delete(self, id):
    assistant = Assistant.get_by_id(int(id), parent=self.get_current_account())

    if not assistant:
      self.session.add_flash(messages.BUS_DRIVER_NOT_FOUND, level='error')
      return self.redirect_to('assistant.list')

    assistant.delete()
    self.session.add_flash(messages.BUS_DRIVER_DELETE_SUCCESS)

    return self.redirect_to('assistant.list')

  @role_required(is_manager=True, is_editor=True)
  def update(self, id):
    assistant = Assistant.get_by_id(int(id), parent=self.get_current_account())

    if not assistant:
      return self.redirect_to('assistant.list', messages.BUS_DRIVER_NOT_FOUND)

    form = AssistantForm(self.request.POST, obj=assistant)

    if self.request.method == 'POST' and form.validate():
      form.populate_obj(assistant)
      assistant.name = ' '.join((form.data['first_name'],
                                  form.data['last_name']))
      assistant.put()

      self.session.add_flash(messages.BUS_DRIVER_UPDATE_SUCCESS)
      return self.redirect_to('assistant.list')

    return self.render_to_response('assistant/form.haml', {'form': form})

  def list(self):
    # We pass form so we can generate it with the modal using macros.
    return self.render_to_response('assistant/list.haml', {'form': AssistantForm()})
