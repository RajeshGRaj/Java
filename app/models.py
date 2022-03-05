from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=500)

    def __str__(self):
        return u'%s' %(self.topic_name)

class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return u'%s' %(self.topic)

class Example(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    example = models.TextField()

    def __str__(self):
        return u'%s' %(self.topic)
