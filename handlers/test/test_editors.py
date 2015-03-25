import unittest2

from wtforms import ValidationError

from library import testing


class TestEditors(testing.TestCase, unittest2.TestCase):

  @testing.login_as
  def test_editor_handler_updates_editor_via_form(self):
    # Retrieves logged in profile, and loads relevant editor's page.
    profile_original = self.get_current_profile()
    response = self.app.get(self.uri_for('editors.update',
                                         id=profile_original.key().id()))
    self.assertOk(response)

    # Ensures that form is properly loaded.
    first_name_field = response.pyquery('input#first_name')
    self.assertLength(1, first_name_field)
    self.assertEqual('first_name', first_name_field.attr['type'])
    self.assertEqual('first_name', first_name_field.attr['name'])

    last_name_field = response.pyquery('input#last_name')
    self.assertLength(1, last_name_field)
    self.assertEqual('last_name', last_name_field.attr['type'])
    self.assertEqual('last_name', last_name_field.attr['name'])

    email_field = response.pyquery('input#email')
    self.assertLength(1, email_field)
    self.assertEqual('email', email_field.attr['type'])
    self.assertEqual('email', email_field.attr['name'])

  @testing.login_as
  def test_editor_profile_is_updated_via_form(self):
    profile = self.get_current_profile()
    profile_update = self.create_profile()
    self.app.post(self.uri_for('editors.update',
                               id=profile_update.key().id()),
                  {'fist_name': 'John',
                   'last_name': 'Doe',
                   'email': 'test11@testing.org'})
    self.assertNotEqual(profile.name, profile_update.name)
    self.assertNotEqual(profile.email, profile_update.email)

  @testing.login_as
  def test_editor_throws_error_when_existing_email_is_used_in_update(self):
    # Assert that error is thrown when a pre-existing email address is entered.
    profile = self.create_profile(email='test@edtest.com')
    self.app.post(self.uri_for('editors.update',
                               id=profile.key().id()),
                  {'email': self.DEFAULT_EMAIL})
    self.assertRaisesRegexp(ValidationError, 'That e-mail is already in use!')
