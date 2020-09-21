from django.db import models

# Create your models here.

class SuccessStory(models.Model):
    story_name = models.CharField(max_length=50)
    date = models.CharField(max_length=25)
    story = models.TextField()
    image = models.ImageField(upload_to='images/',default='images/7.jpg')

    def __str__(self):
        return self.story_name

    

class NewEvent(models.Model):
    eventname = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    

    def __str__(self):
        return self.eventname