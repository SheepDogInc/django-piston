Generating Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

Chances are, if you intend to publicly expose your API, that you want to
supply documentation. Writing documentation is a tedious process, and
even more so if you change things in your code.

Luckily, Piston can do a lot of the heavy lifting for you here as well.

In ``piston.doc`` there is a set of methods, allowing you to easily
generate documentation using standard Django views and templates.

The function ``generate_doc`` returns a ``HandlerDocumentation``
instance, which has a few methods:

-  .model (get\_model) returns the name of the handler,
-  .doc (get\_doc) returns the docstring for the given handler.
-  .get\_methods returns a list of methods available. The optional
   keyword argument ``include_defaults`` (False by default) will also
   include the fallback methods, if you haven’t overloaded them. This
   may be useful if you want to use these, and still include them in
   your documentation.

``get_methods`` yields a set of ``HandlerMethod``’s which are more
interesting:

-  .signature (get\_signature) will return the methods *signature*,
   stripping the first two arguments, which are always ‘self’ and
   ‘request’. The client will not specify these two, so they are not
   interesting. Takes an optional argument, ``parse_optional`` (default
   True), which turns keyword arguments defaulting to None into
   "<optional>".
-  .doc (get\_doc) returns the docstring for an action, so you should
   keep your handler/action specific documentation there.
-  .iter\_args() will yield a 2-tuple with the argument name, and the
   default argument (or None.) If the default argument *is* None, the
   default argument will be ‘None’ (string). This will allow you to
   distinguish whether there is a default argument (even if it’s None),
   or if it’s empty.

For example:

.. sourcecode:: python

    from piston.handler import BaseHandler
    from piston.doc import generate_doc

    class BlogpostHandler(BaseHandler):
        model = Blogpost

        def read(self, request, post_slug=None):
            """
            Reads all blogposts, or a specific blogpost if
            `post_slug` is supplied.
            """
            pass

        @staticmethod
        def resource_uri():
            return ('api_blogpost_handler', ['id'])

    doc = generate_doc(BlogpostHandler)

    print doc.name # -> 'BlogpostHandler'
    print doc.model # -> <class 'Blogpost'>
    print doc.resource_uri_template # -> '/api/post/{id}'

    methods = doc.get_methods()

    for method in methods:
        print method.name # -> 'read'
        print method.signature # -> 'read(post_slug=<optional>)'

        sig = ''

        for argn, argdef in method.iter_args():
            sig += argn

            if argdef:
                sig += "=%s" % argdef

            sig += ', '

        sig = sig.rstrip(",")

        print sig # -> 'read(repo_slug=None)'

Resource URIs
^^^^^^^^^^^^^

Each resource can have an URI. They can be accessed in the Handler via
his .resource\_uri() method.

.. seealso::

    `FAQ: What is a URI Template </jespern/django-piston/wiki/FAQ#what-is-a-uri-template>`_.


