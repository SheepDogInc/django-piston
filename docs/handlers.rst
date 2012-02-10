Configuring Handlers
--------------------

Handlers can be configured with 4 different variables.

Model
^^^^^

The model to tie to. See `Working with
Models </jespern/django-piston/wiki/Documentation#working-with-models>`_.

Fields/Exclude
^^^^^^^^^^^^^^

A list of fields to include or exclude. Accepts nested listing, and
follows foreign keys and manytomany fields. Also accepts compiled
regular expressions. E.g.:

.. sourcecode:: python

    import re

    class FooHandler(BaseHandler):
       fields = ('title', 'content', ('author', ('username', 'first_name')))
       exclude = ('id', re.compile('^private_'))

If User can access posts via a Many2many/ForeignKey fields then:

.. sourcecode:: python

    class UserHandler(BaseHandler):
          model = User
          fields = ('name', ('posts', ('title', 'date')))

will show the title and date from a users posts.

To use the default handler for a nested resource specify an empty list
of fields:

.. sourcecode:: python

    class PostHandler(BaseHandler):
          model = Post
          exclude = ('date',)

    class UserHandler(BaseHandler):
          model = User
          fields = ('name', ('posts', ()))

This UserHandler shows all fields for all posts for a user excluding the
date.

Neither ``fields``, nor ``exclude`` are required, and either one can be
used by itself.

Anonymous
^^^^^^^^^

A pointer to an alternate anonymous resource. See `Anonymous
Resources </jespern/django-piston/wiki/Documentation#anonymous-resources>`_
