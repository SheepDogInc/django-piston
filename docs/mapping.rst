Mapping URLs
------------

URL mappings in Piston work just like they do in Django. Lets map our
BlogpostHandler:

In urls.py:

.. sourcecode:: python

    from django.conf.urls.defaults import *
    from piston.resource import Resource
    from mysite.myapp.api.handlers import BlogpostHandler

    blogpost_handler = Resource(BlogpostHandler)

    urlpatterns = patterns('',
       url(r'^blogpost/(?P<post_slug>[^/]+)/', blogpost_handler),
       url(r'^blogposts/', blogpost_handler),
    )

Now any request coming in to /api/blogpost/some-slug-here/ or
/api/blogposts/ will map to BlogpostHandler, with the two different data
sets being differentiated in the handler itself. Note that a single
handler can be used both for single-object and multiple-object
resources.

Anonymous Resources
^^^^^^^^^^^^^^^^^^^

Resources can also be "anonymous". What does this mean? This is a
special type of resource you can instantiate, and it will be used for
requests that aren’t authorized (via OAuth, Basic or any authentication
handler.)

For example, if we look at our BlogpostHandler from earlier, it might be
interesting to offer anonymous access to posts, although we don’t want
to allow anonymous users to create/update/delete posts. Also, we don’t
want to expose all the fields authorized users see.

This can be done by creating another handler, inheriting
AnonymousBaseHandler (instead of BaseHandler.) This also takes care of
the heavy lifting for you.

Like so:

.. sourcecode:: python

    from piston.handler import AnonymousBaseHandler, BaseHandler

    class AnonymousBlogpostHandler(AnonymousBaseHandler):
       model = Blogpost
       fields = ('title', 'content')

    class BlogpostHandler(BaseHandler):
       anonymous = AnonymousBlogpostHandler
       # same stuff as before

You don’t need a "proxy handler" subclassing BaseHandler to use
anonymous handlers, you can just point directly at an anonymous resource
as well.


