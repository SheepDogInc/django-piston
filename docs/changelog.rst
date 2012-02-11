Change History
~~~~~~~~~~~~~~

0.3.1
^^^^^

:Release Date: 2012-02-11 8:00PM AST
:by:           SheepDogInc.
:Contributors: thurloat, honza, mkaluza, michaelblume, minichate,
               ivangonekrazy, kennthreitz

Important Notes
---------------

First minor release contains a year or work from hard working folks around the
community, mostly. There aren't any backward incompatible changes as we've
tested so far.

The unit tests were brought into piston.tests and added a test runner so you
can run the tests with ``$ python setup.py test``.

Features
--------

  - Add utility shortcut ``piston.utils.direct_to_string``.
    
    - Documentation for :ref:`piston-utils-direct-to-string`
    
  - Add ``MultiAuthentication`` auth option to allow support for multiple Auth
    mechanisms.

    - Documentation for :ref:`piston-authentication-MultiAuthentication`
    - Original thanks to the `Staerr Gist`_

  - Add ``DjangoAuthentication`` auth option for using the API from your own
    client.
    
    - Documentation for :ref:`piston-authentication-DjangoAuthentication`
    - Original thanks to Yann Malet: `Yann Malet Blog Post`_

  - Allow Mimer and translate_mime to be overriden in subclasses of Resource
  - Add Pagination (docs to come, tests passing.)

Fixes
-----

  - Hardening of unit tests, so they don't break all the time.
  - Allowing a dict/list map to be based on a handler callable rather than a
    model property.
  - Support for optional named pk fields
  - Fix setup.py to work again
  - Add initial South migrations.
  - Update OAuth key and secret lookups to be ascii forced for hmac signer.
  - Patch required to let OAuth message signing check to work. (Ignore empty values)
  - More verbose message about registering duplicate models

.. _Staerr Gist: https://gist.github.com/790222
.. _Yann Malet Blog Post: http://yml-blog.blogspot.com/2009/10/django-piston-authentication-against.html>

0.2.3-a
^^^^^^^

For the history of the repo before our contributions, please see the original
changeset on `Bitbucket <https://bitbucket.org/jespern/django-piston/changesets>`_. 


