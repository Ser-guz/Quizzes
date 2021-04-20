from django.urls import path
from . import views


urlpatterns = [
    path("", views.QuizzesView.as_view())
]