from django import forms

from first.models import Comment


class TodoCreatedForm(forms.Form):
    title = forms.CharField(max_length=100)


class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
