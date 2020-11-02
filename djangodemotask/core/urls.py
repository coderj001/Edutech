from django.urls import path
from core.views import (demo, homepage)

app_name = "core"

urlpatterns = [
    path('demo/', demo, name="demo"),
    path('', homepage, name="homepage"),
]
