Streaming
~~~~~~~~~

Since `b0a1571ff61a </jespern/django-piston/changeset/b0a1571ff61a>`_ ,
Piston supports streaming its output to the client. This is **disabled**
per default, for one reason:

-  Django’s support for streaming breaks with
   ``ConditionalGetMiddleware`` and ``CommonMiddleware``.

To get around this, Piston ships with two "proxy middleware classes"
that won’t execute during a streaming scenario, and hence won’t look at
(and exhaust) the data before sending it to the client. Without these,
Django will look at the contents (to figure out E-Tags and
Content-Length), and by doing so, the next peek it takes, will result in
nothing.

In ``piston.middleware`` there are two classes you can effectively
replace these with.

In settings.py:

.. sourcecode:: python

    MIDDLEWARE_CLASSES = (
       # ...
        'piston.middleware.ConditionalMiddlewareCompatProxy',
        'piston.middleware.CommonMiddlewareCompatProxy',
       # ...
    )

Remove any mentions of ``ConditionalGetMiddleware`` and
``CommonMiddleware``, or it **won’t work**. If you have any other
middleware that looks at the content prior to streaming, you can wrap
those in the conditional middleware proxy too:

.. sourcecode:: python

    from piston.middleware import compat_middleware_factory

    class MyMiddleware(...):
       ...

    MyMiddlewareCompatProxy = compat_middleware_factory(MyMiddleware)

And then install ``MyMiddlewareCompatProxy`` instead.
