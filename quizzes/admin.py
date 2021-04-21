from django.contrib import admin
from .models import User, Question, Quiz, AnswerQuestion, Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'category', 'date_created', 'date_start', 'date_end', 'description')


@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    list_display = ('questions', 'answer_text')
