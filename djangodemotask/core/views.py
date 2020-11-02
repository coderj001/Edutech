from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from core.forms import (QuestionForm, SearchForm, )
from core.models import Question
from taggit.models import Tag

# Create your views here.


def demo(request):
    return HttpResponse('Hello World')


def homepage(request):
    context = {}
    return render(request, 'core/homepage.html', context=context)


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
