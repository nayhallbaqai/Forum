from django.conf.urls import url
from forum_app.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^(?P<pk>[-\w]+)/$', CategoryQuestionList.as_view(), name='cat-question-list'),
]