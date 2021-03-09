from django.urls import path
from .views import NewQuestion, getQuestions

urlpatterns = [
    path("", getQuestions, name="khoidong1"),
    path("newQuestion/", NewQuestion.as_view(), name="newKhoiDong1Question"),
]