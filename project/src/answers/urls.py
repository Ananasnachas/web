from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from answers import views


urlpatterns = [
    url(r'^edit/(?P<id>\d+)/$', login_required(views.AnswerEdit.as_view()), name='answer_edit'),
    url(r'^(?P<id>\d+)/create/$', login_required(views.AnswerCreate.as_view()), name='answer_create'),
    ]