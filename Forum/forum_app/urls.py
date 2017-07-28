from django.conf.urls import url
from forum_app.views import *

urlpatterns = [
    url(r'^', IndexView.as_view()),
]