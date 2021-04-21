from django.urls import path
from . import views


urlpatterns = [
    path("", views.QuizListView.as_view()),
    path("<int:pk>/", views.QuizDetailsView.as_view()),
]