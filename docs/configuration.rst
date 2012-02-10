Configuration variables
-----------------------

Piston is configurable in a couple of ways, which allows more granular
control of some areas without editing the code.

+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                            | Meaning                                                                                                                                                                                |
+====================================+========================================================================================================================================================================================+
| settings.PISTON\_EMAIL\_ERRORS     | If (when) Piston crashes, it will email the administrators a backtrace (like the Django one you see during DEBUG = True)                                                               |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| settings.PISTON\_DISPLAY\_ERRORS   | Upon crashing, will display a small backtrace to the client, including the method signature expected.                                                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| settings.PISTON\_STREAM\_OUTPUT    | When enabled, Piston will instruct Django to stream the output to the client, but please read `streaming </jespern/django-piston/wiki/Documentation#streaming>`_ before enabling it.   |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
