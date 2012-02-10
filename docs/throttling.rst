Throttling
----------

Sometimes you may not want people to call a certain action many times in
a short period of time. Piston allows you to throttle requests on a
global basis, effectively denying them access until the throttle has
expired.

Piston will respect OAuth (if used) and limit on a per-consumer basis.
If OAuth is not used, Piston will resort to the logged in user, and for
anonymous requests, it will fall back to the clients IP address.

Throttling can be enabled via the special @throttle decorator. It takes
2 required arguments, and an optional third argument.

The first argument is the number of requests allowed to be made within a
certain amount of seconds. The second argument is the number of seconds.
The third argument is optional, and should be a string, which will be
appended to the cache key, effectively allowing you to do special
throttling for a single action, or group several actions together. If
omitted, the throttle will be global.

For example:

.. sourcecode:: python

    @throttle(5, 10*60)
    def create(...

This will throttle if the client calls ‘create’ more than 5 times within
10 minutes.

You can do grouping like so:

.. sourcecode:: python

    @throttle(5, 10*60, 'user_writes')
    def create(...

    @throttle(5, 10*60, 'user_writes')
    def update(...
