from views import *
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^list/$',
        ListView.as_view(),
        name="list"),
    )
