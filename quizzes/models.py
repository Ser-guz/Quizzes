from django.db import models


class User(models.Model):
    """Пользователи"""
    name = models.CharField("Имя пользователя", max_length=150, unique=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    """Категория опроса"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Question(models.Model):
    """Вопрос"""
    question_text = models.CharField("Вопрос", max_length=150)
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Quiz(models.Model):
    """Опрос"""
    name = models.CharField("Название", max_length=150)
    image = models.ImageField("Фото", upload_to="quizzes/", null=True)
    description = models.TextField("Описание")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_start = models.DateTimeField("Начало опроса")
    date_end = models.DateTimeField("Завершение опроса")
    status = models.BooleanField("Активен", default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, verbose_name="вопрос")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class AnswerQuestion(models.Model):
    """Ответ на вопрос"""
    answer_text = models.TextField("Ответ")
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответ"
