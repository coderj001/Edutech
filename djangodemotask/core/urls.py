from django.urls import path
from core.views import (demo,)

urlpatterns = [
    path('', demo, name="demo"),
]
