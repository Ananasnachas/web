from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from users.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UsersListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('first_name', 'Name ack'),
        ('-first_name', 'Name desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)

