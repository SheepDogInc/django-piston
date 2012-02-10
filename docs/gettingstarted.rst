Getting Started
---------------

Getting started with Piston is easy. Your API code will look and behave just
like any other Django application. It will have an URL mapping and handlers
defining resources.

To get started, it is recommended that you place your API code in a separate
folder, e.g. ‘api’.

Your application layout could look like this:

::

    urls.py
    settings.py
    myapp/
       __init__.py
       views.py
       models.py
    api/
       __init__.py
       urls.py
       handlers.py

Then, define a "namespace" where your API will live in your top-level
urls.py, like so:

.. sourcecode:: python

    urlpatterns = patterns('',
       # all my other url mappings
       (r'^api/', include('mysite.api.urls')),
    )

This will include the API’s urls.py for anything beginning with ‘api/’.

Next up we’ll look at how we can create resources and how to map URLs to
them.
