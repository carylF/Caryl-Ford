from webapp2_extras.routes import RedirectRoute

from handlers.home import HomeHandler
from handlers.login import LoginHandler
from handlers.profile import ProfileHandler
from handlers.signup import SignupHandler
from handlers.static import PublicStaticHandler
from handlers.contact import ContactHandler
from handlers.editor import EditorHandler
from handlers.activity import ActivityHandler
from handlers.assistant import AssistantHandler
from handlers.instructor import InstructorHandler


__all__ = ['application_routes']

application_routes = []

_route_info = [
    # Public (static) handlers.
    ('about', 'GET', '/about/',
        PublicStaticHandler('about.haml'), 'get'),
    ('copyright', 'GET', '/copyright/',
        PublicStaticHandler('coming_soon.haml'), 'get'),
    ('faq', 'GET', '/faq/',
        PublicStaticHandler('coming_soon.haml'), 'get'),
    ('features', 'GET', '/features/',
        PublicStaticHandler('coming_soon.haml'), 'get'),
    ('privacy', 'GET', '/privacy/',
        PublicStaticHandler('coming_soon.haml'), 'get'),
    ('terms', 'GET', '/terms/',
        PublicStaticHandler('coming_soon.haml'), 'get'),

    # Public handlers.
    ('contact', None, '/contact/', ContactHandler, 'contact'),
    ('home', 'GET', '/', HomeHandler, 'home'),
    ('signup', None, '/signup/', SignupHandler, 'signup'),

    # Authentication-related handlers.
    ('login', None, '/login/', LoginHandler, 'login'),
    ('logout', 'GET', '/logout/', LoginHandler, 'logout'),
    ('forgot-password', None, '/forgot-password/',
        LoginHandler, 'forgot_password'),

    ('profile.activate', None, '/profile/activate/',
        ProfileHandler, 'activate'),
    ('profile.view', None, '/profile/', ProfileHandler, 'view'),

    ('activity.create', None, '/activity/create/', ActivityHandler, 'create'),
    ('activity.delete', None, '/activity/<id:\d+>/delete/',
        ActivityHandler, 'delete'),
    ('activity.update_times', None, '/activity/<id:\d+>/update_times/',
        ActivityHandler, 'update_times'),
    ('activity.assign_assistant', None, '/activity/<id:\d+>/assign_assistant/',
        ActivityHandler, 'assign_driver'),
    ('activity.list', None, '/activity/', ActivityHandler, 'list'),
    ('activity.update', None, '/activity/<id:\d+>/update/',
        ActivityHandler, 'update'),

    ('assistant.create', None, '/assistant/create/', AssistantHandler, 'create'),
    ('assistant.delete', None, '/assistant/<id:\d+>/delete/',
        AssistantHandler, 'delete'),
    ('assistant.list', None, '/assistant/', AssistantHandler, 'list'),
    ('assistant.update', None, '/assistant/<id:\d+>/update/',
        AssistantHandler, 'update'),

    ('instructor.create', None, '/instructor/create/', InstructorHandler, 'create'),
    ('instructor.delete', None, '/instructor/<id:\d+>/delete/',
        InstructorHandler, 'delete'),
    ('instructor.list', None, '/instructor/', InstructorHandler, 'list'),
    ('instructor.update', None, '/instructor/<id:\d+>/update/',
        InstructorHandler, 'update'),
]

for name, methods, pattern, handler_cls, handler_method in _route_info:
  # Allow a single string, but this has to be changed to a list.
  if isinstance(methods, basestring):
    methods = [methods]

  # Create the route.
  route = RedirectRoute(name=name, template=pattern, methods=methods,
                        handler=handler_cls, handler_method=handler_method)

  # Add the route to the proper public list.
  application_routes.append(route)
