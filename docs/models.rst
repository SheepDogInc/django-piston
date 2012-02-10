Working with Models
-------------------

Piston allows you to tie to a model, but does not require it. The
benefit you get from doing so, will become obvious when you work with
it:

-  If you don’t override read/create/update/delete it provides sensible
   defaults (if the method is allowed by ``allow_methods`` of course.)
-  You don’t have to specify ``fields`` or ``exclude`` (but you still
   can, they aren’t mutually exclusive!)
-  By using a model in a handler, Piston will remember your
   ``fields``/``exclude`` directives and use them in other handlers who
   return objects of that type (unless overridden.)

As we’ve seen earlier, tying to a model is as simple as setting the
``model`` class variable on a handler.

.. seealso::

    `Why does Piston use fields from previous handlers 
    <http://bitbucket.org/jespern/django-piston/wiki/FAQ#why-does-piston-use-fields-from-previous-handlers>`_


