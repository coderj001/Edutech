from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from core.forms import QuestionForm
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
        pass
