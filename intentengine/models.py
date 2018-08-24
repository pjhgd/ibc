from django.db import models

# Create your models here.

class branchxmlfiles(models.Model):
    pkid = models.AutoField(primary_key=True)
    template = models.IntegerField()
    xml = models.CharField(max_length=2000)
    datecreated = models.DateField(auto_now_add=True)

class provisioningstatus(models.Model):
    pkid = models.AutoField(primary_key=True)
    intent = models.CharField(max_length=2000)
    submittime = models.DateTimeField(auto_now_add=True)
    provisionTaskId = models.IntegerField(default=0)
    status = models.CharField(max_length=2000)

