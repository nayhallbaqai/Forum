from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


class Question(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Answer(models.Model):
    comment = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)