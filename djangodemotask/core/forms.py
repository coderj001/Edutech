from django import forms
from core.models import (Question, Answer)
from taggit.forms import TagField
from django.contrib.auth import authenticate


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


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'text',
        ]


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect.')
            if not user.check_password(password):
                raise forms.ValidationError('Not password incorrect')
            if not user.is_active:
                raise forms.ValidationError('plus valide')
        return super().clean(*args, **kwargs)
