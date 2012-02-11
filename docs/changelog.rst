Change History
~~~~~~~~~~~~~~

0.3.1
^^^^^

:Release Date:        2012-02-10 8:00PM AST
:by:                  SheepDogInc.
:GitHub Contributors: thurloat, honza, mkaluza, michaelblume, minichate,
                      ivangonekrazy, kennthreitz

Important Notes
---------------

First minor release contains a year or work from hard working folks around the
community, mostly. There aren't any backward incompatible changes as we've
tested so far.

Features
--------

  - Add shortcut ``piston.utils.render_to_string``.
  - Add ``MultiAuthentication`` auth option to allow support for multiple Auth
    mechanisms.
    Original thanks to ``@staerr``: `Gist <https://gist.github.com/790222>`_
  - Add ``DjangoAuthentication`` auth option for using the API from your own
    client.
    Original thanks to Yann Malet: `Original Post 
    <http://yml-blog.blogspot.com/2009/10/django-piston-authentication-against.html>`_
  - Allow Mimer and translate_mime to be overriden in subclasses of Resource
  - Add Pagination (docs to come)

Fixes
-----

  - Allowing a dict/list map to be based on a handler callable rather than a
    model property.
  - Support for optional named pk fields
  - Fix setup.py to work again
  - Add initial South migrations.
  - Update OAuth key and secret lookups to be ascii forced for hmac signer.
  - Patch required to let OAuth message signing check to work. (Ignore empty values)
  - More verbose message about registering duplicate models

0.2.3-a
^^^^^^^

For the history of the repo before our contributions, please see the original
changeset on `Bitbucket <https://bitbucket.org/jespern/django-piston/changesets>`_. 


