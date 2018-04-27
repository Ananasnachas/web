from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
]