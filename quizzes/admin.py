from django.contrib import admin
from .models import User, Question, Quiz, AnswerQuestion

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(AnswerQuestion)

