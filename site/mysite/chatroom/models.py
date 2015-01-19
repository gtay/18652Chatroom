import datetime
from django.db import models

from django.contrib.auth.models import User

class Message(models.Model):
    text = models.CharField(max_length=500)
    time_stamp = models.DateTimeField('timestamp', default=datetime.datetime.now)
    #name = models.ForeignKey(User, default=User.objects.get(id=1))
    name = models.CharField(max_length=50, default='')
    def __unicode__(self):
        return self.text

# Create your models here.
