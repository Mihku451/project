from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=42)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.now)
    # неположительные значение <=> неограниченные кол-во попыток,
    limit_of_tries = models.SmallIntegerField(default=1, blank=True)
    time = models.IntegerField(default=120)
    # отвечает за показывание правильных ответов теста после прохождения


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    image = models.ImageField(default=None)
    score = models.SmallIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.question_text


TYPES = (
    ('radio', 'один из'),
    ('checkbox', 'несколько из'),
    ('textbox', 'Ввод текста'),
)


class Answer(models.Model):
    answer_type = models.CharField(max_length=16, choices=TYPES, default="radio")
    # сколько баллов дается если ответ правильный

    # текст вар. ответа
    answer_text = models.CharField(max_length=32, blank=True)
    # правильность ответа
    is_valid = models.BooleanField(default=False)
    # Вводятся.
    user_answer = models.CharField(max_length=32, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ResultsPassing(models.Model):
    pupil = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    used_time = models.IntegerField(default=0)
    answers = models.ManyToManyField(Answer)
    score = models.IntegerField(default=0)
