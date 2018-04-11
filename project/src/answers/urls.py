from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from answers import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.answer_detail, name='answer_detail'),
    url(r'^(?P<id>\d+)/edit/$', login_required(views.AnswerEdit.as_view()), name='answer_edit'),
    url(r'^create/$', login_required(views.AnswerCreate.as_view()), name='answer_create'),
]