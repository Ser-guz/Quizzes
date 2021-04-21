from django.shortcuts import render
from django.views.generic.base import View

from .models import Quiz, Category, AnswerQuestion


class QuizListView(View):
    """Список опросов"""
    def get(self, request):
        quizzes = Quiz.objects.all()
        categories = Category.objects.all()
        return render(request, 'quizzes/quiz_list.html', {'quiz_list': quizzes,
                                                          'category_list': categories})


class QuizDetailsView(View):
    """Полное описание опроса"""
    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        answers = AnswerQuestion.objects.all()
        return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz,
                                                            'answer_list': answers})