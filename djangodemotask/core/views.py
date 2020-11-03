from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import gettext as _
from core.forms import (QuestionForm, SearchForm, AnswerForm, UserLoginForm)
from core.models import (Question, Answer)
from taggit.models import Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def demo(request):
    return HttpResponse('Hello World')


def homepage(request):
    context = {}
    return render(request, 'core/homepage.html', context=context)


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:homepage')
        else:
            return render(request, 'core/signup.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("core:homepage")


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.GET['next'])
                except:
                    return redirect('core:homepage')
            else:
                return render(request, 'core/login.html', {'form': form})
        else:
            return render(request, 'core/login.html', {'form': form})
    form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})


def ask_question(request):

    if request.method == "POST":
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            form.save_m2m()
            return redirect("core:homepage")
        context = {'form': form}
        return render(request, 'core/ask_question.html', context=context)

    if request.method == "GET":
        form = QuestionForm()
        context = {'form': form}
        return render(request, 'core/ask_question.html', context=context)


def search_question(request):
    if request.method == "GET":
        form = SearchForm()
        questions = Question.objects.all()
        context = {
            'form': form,
            'questions': questions,
        }
        return render(request, 'core/search_question.html', context=context)
    if request.method == "POST":
        form = SearchForm(request.POST or None)
        context = {}
        if form.is_valid():
            title = form.cleaned_data['title']
            tags = form.cleaned_data['tags']
            if not tags:
                qu = Question.objects.filter(title__icontains=title)
            else:
                qu = Question.objects.filter(title__icontains=title).filter(
                    tags__name__in=tags).distinct()
            context['questions'] = qu
        context['form'] = form
        return render(request, 'core/search_question.html', context=context)


def question(request, id):
    question = get_object_or_404(Question, id=id)
    context = {}
    context['question'] = question
    if request.method == 'GET':
        form = AnswerForm()
        context['form'] = form
    if request.method == 'POST':
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_by = request.user
            answer.question = question
            form.save()
            form = AnswerForm()
        context['form'] = form
    return render(request, 'core/question.html', context=context)
