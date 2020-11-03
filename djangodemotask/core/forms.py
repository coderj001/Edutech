from django import forms
from core.models import (Question, Answer)
from taggit.forms import TagField
from django.contrib.auth import authenticate


class QuestionForm(forms.ModelForm):
    """ Form For Question Model """
    class Meta:
        model = Question
        fields = [
            'title',
            'description',
            'tags',
        ]


class SearchForm(forms.Form):
    """ Form for valid search and feed result """
    title = forms.CharField(max_length=255, required=False, label='Title')
    tags = TagField(max_length=100, label='Tags', required=False)


class AnswerForm(forms.ModelForm):
    """ Form for answer model """
    class Meta:
        model = Answer
        fields = [
            'text',
        ]


class UserLoginForm(forms.Form):
    """ UserLoginForm similar to  usercreationform of django for for authenticate valid user """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        """ For getting clean username and password input """

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
