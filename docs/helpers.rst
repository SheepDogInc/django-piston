Helpers, utils & @decorators
----------------------------

For your convenience, there’s a set of helpers and utilities you can
use. One of those is ``rc`` from ``piston.utils``. It contains a set of
standard returns that you can return from your actions to indicate a
certain situation to the client.

Since `26293e3884f4 </jespern/django-piston/changeset/26293e3884f4>`_ ,
these return a **fresh** instance of HttpResponse, so you can use
something like this:

.. sourcecode:: python

    resp = rc.CREATED
    resp.write("Everything went fine!")
    return resp

    resp = rc.CREATED
    resp.write("This will not have the previous 'fine' text in it.")
    return resp

This change is backwards compatible, as it overrides ``__getattr__`` to
return a new instance rather than a singleton.

+-----------------------+------------------------------------+-----------------------------------------+
| Variable              | Result                             | Description                             |
+=======================+====================================+=========================================+
| rc.ALL\_OK            | 200 OK                             | Everything went well.                   |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.CREATED            | 201 Created                        | Object was created.                     |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.DELETED            | 204 (Empty body, as per RFC2616)   | Object was deleted.                     |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.BAD\_REQUEST       | 400 Bad Request                    | Request was malformed/not understood.   |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.FORBIDDEN          | 401 Forbidden                      | Permission denied.                      |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.NOT\_FOUND         | 404 Not Found                      | Resource not found.                     |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.DUPLICATE\_ENTRY   | 409 Conflict/Duplicate             | Object already exists.                  |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.NOT\_HERE          | 410 Gone                           | Object does not exist.                  |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.NOT\_IMPLEMENTED   | 501 Not Implemented                | Action not available.                   |
+-----------------------+------------------------------------+-----------------------------------------+
| rc.THROTTLED          | 503 Throttled                      | Request was throttled.                  |
+-----------------------+------------------------------------+-----------------------------------------+


