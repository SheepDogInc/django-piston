Resources
---------

A "Resource" is an entity mapping some kind of resource in code. This
could be a blog post, a forum or even something completely arbitrary.

Let’s start out by creating a simple handler in handlers.py:

.. sourcecode:: python

    from piston.handler import BaseHandler
    from myapp.models import Blogpost

    class BlogpostHandler(BaseHandler):
       allowed_methods = ('GET',)
       model = Blogpost

       def read(self, request, post_slug):
          ...

Piston lets you map resource to models, and by doing so, it will do a
lot of the heavy lifting for you.

A resource can be just a class, but usually you would want to define at
least 1 of 4 methods:

``read`` is called on GET requests, and should never modify data
(idempotent.)

``create`` is called on POST, and creates new objects, and should return
them (or rc.CREATED.)

``update`` is called on PUT, and should update an existing product and
return them (or rc.ALL\_OK.)

``delete`` is called on DELETE, and should delete an existing object.
Should not return anything, just rc.DELETED.

In addition to these, you may define any other methods you want. You can
use these by including their names in the ``fields`` directive, and by
doing so, the function will be called with a single argument: The
instance of the ``model``. It can then return anything, and the return
value will be used as the value for that key.

.. note:: 

    These "resource methods" should be decorated with the @classmethod
    decorator, as they will not always receive an instance of itself. For
    example, if you have a UserHandler defined, and you return a User from
    another handler, you will not receive an instance of that handler, but
    rather the UserHandler.

Since a single handler can be responsible for both single- and
multiple-object data sets, you can differentiate between them in the
read() method like so:

.. sourcecode:: python

    from piston.handler import BaseHandler
    from myapp.models import Blogpost

    class BlogpostHandler(BaseHandler):
        allowed_methods = ('GET',)
        model = Blogpost

        def read(self, request, blogpost_id=None):
            """
            Returns a single post if `blogpost_id` is given,
            otherwise a subset.
            """
            base = Blogpost.objects

            if blogpost_id:
                return base.get(pk=blogpost_id)
            else:
                return base.all() # Or base.filter(...)



