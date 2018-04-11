from django.conf.urls import url
from tags import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.tag_detail, name='tag_detail'),
    url(r'^$', views.tags_list, name='tags_list'),
]