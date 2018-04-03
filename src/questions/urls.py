from django.conf.urls import url
from questions import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^$', views.questions_list, name='questions_list'),
]