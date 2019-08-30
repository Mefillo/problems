from django.db import models


class Problem (models.Model):
    text = models.TextField(null=True)
    number = models.IntegerField(unique=True, default=0)
    likes = models.IntegerField(unique=False, default=0)

    def __str__(self):
        return self.text


class Solution (models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    number = models.IntegerField(unique=True, default=0)
    likes = models.IntegerField(unique=False, default=0)
    
    def __str__(self):
        return self.text
