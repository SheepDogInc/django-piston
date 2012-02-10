Receiving data
--------------

Piston, being layered on HTTP, works well with post-data (form data),
but also works well with more expressive formats such as JSON and YAML.

This allows you to receive structured data easily, rather than just
key-value pairs. Piston will attempt to deserialize incoming non-form
data via a set of "loaders", depending on the Content-type specified by
the client.

For example, if we send JSON to a handler giving the content-type
"application/json", Piston will do 2 things:

#. Place the deserialized data in ``request.data``, and
#. Set ``request.content_type`` to ``application/json``. For form data,
   this will always be None.

You can use it like so (from
`testapp/handlers.py <http://bitbucket.org/jespern/django-piston/src/7042cd328873/tests/test_project/apps/testapp/handlers.py#cl-31>`_):

.. sourcecode:: python

        def create(self, request):
            if request.content_type:
                data = request.data

                em = self.model(title=data['title'], content=data['content'])
                em.save()

                for comment in data['comments']:
                    Comment(parent=em, content=comment['content']).save()

                return rc.CREATED
            else:
                super(ExpressiveTestModel, self).create(request)

If we send the following JSON structure into that, it will handle it
appropriately:

::

    {"content": "test", "comments": [{"content": "test1"}, {"content": "test2"}], "title": "test"}

It should be noted that sending *anything* that deserializes to this
handler will also work, so you can send equally formatted YAML or XML,
and the handler won’t care.

If your handler doesn’t accept post data (maybe it requires more verbose
data), there’s an easy way to require a specific type of data, via the
``utils.require_mime`` decorator.

This decorator takes a list of types it requires, and you can use the
shorthand too, like ‘yaml’, ‘json’, etc.

There’s also a shortcut for requiring ‘json’, ‘yaml’, ‘xml’ and ‘pickle’
all in one, called ‘require\_extended’.

.. sourcecode:: python

    class SomeHandler(BaseHandler):

        @require_mime('json', 'yaml')
        def create(self):
            pass

        @require_extended
        def update(self):
            pass
