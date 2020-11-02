from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Create your views here.


def demo(request):
    return HttpResponse('Hello World')


def homepage(request):
    context = {
        'hello': _("Hello World")
    }
    return render(request, 'core/homepage.html', context=context)
