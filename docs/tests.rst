Tests
-----

`zerok </zerok>`_ wrote an initial testsuite for Piston, located in
tests/. It uses zc.buildout to run the tests, and isolates an
environment with Django, etc. The suite comes with two testrunners:
tests/bin/test–1.0 and tests/bin/test–1.1 which run the tests against
the respective version of Django and are made available after you’re
finished with the first two steps as described below.

Running the tests is very easy:

::

    $ python bootstrap.py
    Creating directory './bin'.
    [snip]
    Generated script './bin/buildout'.

    $ ./bin/buildout -v
    Develop: 'tests/..'
    Getting distribution for 'djangorecipe'.
    Got djangorecipe 0.17.3.
    Getting distribution for 'zc.recipe.egg'.
    Got zc.recipe.egg 1.2.2.
    Uninstalling django-1.0.
    Installing django-1.0.
    django: Downloading Django from: http://www.djangoproject.com/download/1.0.2/tarball/
    Generated script './bin/django-1.0'.
    Generated script './bin/test-1.0'.

    $ ./bin/test-1.0
    Creating test database...
    [snip]
    ...
    ----------------------------------------------------------------------
    Ran 6 tests in 0.283s

    OK
    Destroying test database...

When running buildout make sure to pass it the -v option. There is
currently a small problem with djangorecipe, which is used to create the
testscripts etc., that causes the script to hang unless you use the "-v"
option.

If you’d like to contribute, more tests are always welcome. There is
coverage for many of the basic operations, but not 100%.


