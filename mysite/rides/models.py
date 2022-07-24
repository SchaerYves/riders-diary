import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Athlete(models.Model):
    athlete_id = models.IntegerField("athlete id")
    vote = models.IntegerField(default = 0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def full_name(self):
        return self.first_name + " " + self.last_name
    def __str__(self):
        return self.first_name + " " + self.last_name

class Activity(models.Model):
    activity_id = models.IntegerField("activity id")
    def __str__(self):
        return self.activity_id
        