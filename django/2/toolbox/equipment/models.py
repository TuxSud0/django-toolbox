from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#PROJECT_NAME = 'Sulfur Reliability'
#PROJECT_NUMBER = '07OT89XX'
#PROJECT_SITE = 'Garyville, LA'

#CLIENT_CHOICES = []
#CLIENT_LOCATIONS = []

class Equipment(models.Model):
    tag = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    location = models.CharField(max_length=20,blank=True, null=True)
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True)
    attachments = models.FileField(upload_to='attachments/', blank=True)

    def __str__(self):
	    return str(self.id)