from django.db import models
# from authUser.models import *
from django.conf import settings

# from authUser.models import User


# Create your models here.

class Gas(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gas_code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'gas'


class GasStatus(models.Model):
    percent = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)
    # is_connected = models.BooleanField(default=True)
    gas = models.ForeignKey(Gas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.percent}'

    class Meta:
        db_table = 'gas_status'

# class Question(models.Model):
#     question = models.TextField()
#     vacancy_id = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, null=True)
#     is_checkable = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'question'
#
#     def __str__(self):
#         return self.question
#
#
# class Answer(models.Model):
#     answer = models.CharField(max_length=200)
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'answer'
#
#     def __str__(self):
#         return f'question {self.question_id.question} answer {self.answer}'
