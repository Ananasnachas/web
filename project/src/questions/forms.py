from django import forms


class QuestionForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    text = forms.CharField(max_length=5000, required=True, widget=forms.Textarea())
    tags = forms.CharField(max_length=255, required=True)


class QuestionsListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('name', 'Name ack'),
        ('-name', 'Name desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)