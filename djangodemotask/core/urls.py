from django.urls import path
from core.views import (demo, homepage, ask_question,
                        search_question, question)

app_name = "core"

urlpatterns = [
    path('demo/', demo, name="demo"),
    path('', homepage, name="homepage"),
    path('ask_question/', ask_question, name="ask_question"),
    path('search_question/', search_question, name="search_question"),
    path('question/<int:id>/', question, name="question"),
]
