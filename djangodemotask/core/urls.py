from django.urls import path
from core.views import (demo, homepage, ask_question,
                        search_question, question, signup_user, logout_user, login_user)

app_name = "core"

urlpatterns = [
    path('demo/', demo, name="demo"),
    path('', homepage, name="homepage"),
    path('ask_question/', ask_question, name="ask_question"),
    path('search_question/', search_question, name="search_question"),
    path('question/<int:id>/', question, name="question"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('signup/', signup_user, name="signup"),
]
