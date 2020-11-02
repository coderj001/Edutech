from django import forms
from core.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'description',
            'tags',
        ]


class SearchForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'tags',
        ]
