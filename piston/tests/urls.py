from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'api/', include('piston.tests.testapp.urls'))
)
