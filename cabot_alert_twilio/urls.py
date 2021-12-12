from django.urls import re_path
from .views import twiml_callback

urlpatterns = [
    re_path(r'^result/(?P<service_id>\d+)/twiml_callback/', twiml_callback, name="twiml-callback"),
]
