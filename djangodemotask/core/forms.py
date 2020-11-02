from django import forms
from core.models import Question
from taggit.forms import TagField


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'description',
            'tags',
        ]


class SearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label='Title')
    tags = TagField(max_length=100, label='Tags', required=False)
