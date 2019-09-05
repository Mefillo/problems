from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User

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


class Utoken (models.Model):
    '''Save likes to User'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problems = JSONField(default = {'':0})
    solutions = JSONField(default = {'':0})