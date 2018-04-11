from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from questions import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<id>\d+)/edit/$', login_required(views.question_edit), name='question_edit'),
    url(r'^$', views.questions_list, name='questions_list'),
    url(r'^create/$', login_required(views.question_create), name='question_create'),
]