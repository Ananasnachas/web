from django import forms


class TagsListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('name', 'Name ack'),
        ('-name', 'Name desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)