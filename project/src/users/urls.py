from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from users import views

urlpatterns = [
    url(r'^$', views.users_list, name='users_list'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', login_required(views.Logout.as_view()), name='logout'),
    url(r'^(?P<id>\d+)/$', views.profile, name='profile'),
    url(r'^my_profile/$', login_required(views.my_profile), name='my_profile'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^my_profile/change_password/$', login_required(views.password_edit), name='password_edit'),
]