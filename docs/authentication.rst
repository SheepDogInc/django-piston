Authentication
~~~~~~~~~~~~~~

Piston comes with 4 built-in authentication mechanisms:

 - ``piston.authentication.NoAuthentication``
 - ``piston.authentication.HttpBasicAuthentication``
 - ``piston.authentication.OAuthAuthentication``
 - ``piston.authentication.DjangoAuthentication``

plus a bonus ``piston.authentication.MultiAuthentication`` class to allow you
to register multiple Auth mechanisms with a single instance of a handler.

The default Authentication mechanism for a handler is ``NoAuthentication``
which simply returns true on ``is_authenticated``.

HttpBasicAuthentication
^^^^^^^^^^^^^^^^^^^^^^^

The ``piston.authentication.HttpBasicAuthentication`` Authentication handler
allows you to use simple HTTP Authentication with your API.

.. note::

    Using ``piston.authentication.HttpBasicAuthentication``
    with apache and mod\_wsgi requires you to add the
    ``WSGIPassAuthorization On`` directive to the server or vhost config,
    otherwise django-piston cannot read the authentication data from
    ``HTTP_AUTHORIZATION`` in ``request.META``. See:
    `Configuration Directives <http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIPassAuthorization>`_.

**Example**

Adding to the Blogpost example, you could require Basic Authentication as 
follows:

.. sourcecode:: python

    from django.conf.urls.defaults import *
    from piston.resource import Resource
    from piston.authentication import HttpBasicAuthentication
    from mysite.myapp.api.handlers import BlogpostHandler

    auth = HttpBasicAuthentication(realm="Django Piston Example")
    blogpost_handler = Resource(BlogpostHandler, authentication=auth)
    urlpatterns = patterns('',
       url(r'^blogpost/(?P<post_slug>[^/]+)/', blogpost_handler),
       url(r'^blogposts/', blogpost_handler),
    )

.. _piston-authentication-DjangoAuthentication:

DjangoAuthentication
^^^^^^^^^^^^^^^^^^^^

A very handy class to use your API from pages that Django rendered, 
``DjangoAuthentication`` allows you to use a user's session cookie to
Authenticate to the API.

OAuthAuthentication
^^^^^^^^^^^^^^^^^^^

OAuth is the preferred means of authorization, because it distinguishes
between "consumers", i.e. the approved application on your end which is
using the API. Piston knows and respects this, and makes good use of it,
for example when you use the @throttle decorator, it will limit on a
per-consumer basis, keeping services operational even if one service has
been throttled.

.. _piston-authentication-MultiAuthentication:

MultiAuthentication
^^^^^^^^^^^^^^^^^^^

``MultiAuthentication`` allows you to register multiple authentication classes
for the same handler.

On each call, it will try each auth method in order, and try to authenticate in
before failing.

**Example**

This example shows registering all 3 Auth methods to a single handler inside
the url configuration in ``urls.py``.

.. sourcecode:: python

    dj_auth = DjangoAuthentication()
    basic_auth = HttpBasicAuthentication(realm="BasicAuth")
    o_auth = OAuthAuthentication(realm="OAuth")

    # Register all 3 Auth methods for the API.
    auth = MultiAuthentication([dj_auth, basic_auth, o_auth])
    ad = { 'authentication': auth }

    # User Handler
    user_handler = APIResource(UserHandler, \*\*ad)
        

Build Your Own
^^^^^^^^^^^^^^

Piston supports pluggable authentication through a simple interface.
Resources can be initialized to use any authentication handler that
implements the interface. 

The Basic auth handler is very simple, and you should use this for reference if you want to roll
your own.

An authentication handler is a class, which must have 2 methods:
``is_authenticated`` and ``challenge``.

``is_authenticated`` will receive exactly 1 argument, a copy of the
``request`` object Django receives. This object will hold all the
information you will need to authenticate a user, e.g.
``request.META.get('HTTP_AUTHENTICATION')``.

Upon successful authentication, this function must set ``request.user``
to the correct ``django.contrib.auth.models.User`` object. This allows
for subsequent handlers to identify who is logged in.

It must return either True or False, indicating whether the user was
logged in.

For cases where authentication fails, is where ``challenge`` comes in.

``challenge`` will receive no arguments, and must return a
``HttpResponse`` containing the proper challenge instructions. For Basic
auth, it will return an empty response, with the header
``WWW-Authenticate`` set, and status code 401. This will tell the
receiving end that they need to supply us with authentication.

For anonymous handlers, there is a special class, ``NoAuthentication``
in ``piston.authentication`` that always returns True for
``is_authenticated``.








