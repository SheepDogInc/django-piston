Emitters
--------

Emitters are what spews out the data, and are the things responsible for
speaking YAML, JSON, XML, Pickle and Django. They currently reside in
``emitters.py`` as ``XMLEmitter``, ``JSONEmitter``, ``YAMLEmitter``,
``PickleEmitter`` and ``DjangoEmitter``.

Writing your own emitters is easy, all you have to do is create a class
that subclasses ``Emitter`` and has a ``render`` method. The render
method will receive 1 argument, ‘request’, which is a copy of the
request object, which is useful if you need to look at request.GET (like
defining callbacks, like the JSON emitter does.)

To get the data to serialize/render, you can call ``self.construct()``
which always returns a dictionary. From there, you can do whatever you
want with the data and return it (as a unicode string.)

.. note:: 

    New in `23ebc37c78e8 </jespern/django-piston/changeset/23ebc37c78e8>`_ :
    Emitters can now be registered with the ``Emitter.register`` function,
    and can be removed (in case you want to remove a built-in emitter) via
    the ``Emitter.unregister`` function.

The built-in emitters are registered like so:

.. sourcecode:: python

    class JSONEmitter(Emitter):
       ...

    Emitter.register('json', JSONEmitter, 'application/json; charset=utf-8')

If you write your own emitters, you can import Emitter and call
‘register’ on it to put your emitter into action. You can also overwrite
built-in, or existing emitters, by using the same name (the first
argument.)

This makes it very easy to add support for extended formats, like
protocol buffers or CSV.

Emitters are accessed via the ?format GET argument, e.g.
‘/api/blogposts/?format=yaml’, but since
`23ebc37c78e8 </jespern/django-piston/changeset/23ebc37c78e8>`_ , it is
now possible to access them via a special keyword argument in your URL
mapping. This keyword is called ‘emitter\_format’ (to not clash with
your own ‘format’ keyword), and can be used like so:

.. sourcecode:: python

    urlpatterns = patterns('',
       url(r'^blogposts(?P<emitter_format>.+)$', ...),
    )

Now a request for /blogposts.json will use the JSON emitter, etc.

Additionally, you may specify the format in your URL mapping, via the
keyword arguments shortcut:

.. sourcecode:: python

    urlpatterns = patterns('',
       url(r'^blogposts$', resource_here, { 'emitter_format': 'json' }),
    )


