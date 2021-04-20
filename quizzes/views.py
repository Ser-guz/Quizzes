from django.shortcuts import render
from django.views.generic.base import View

from .models import Quiz


class QuizzesView(View):
    """Список опросов"""
    def get(self, request):
        quizzes = Quiz.objects.all()
        return render(request, 'quizzes/quizzes.html', {'quiz_list': quizzes})
