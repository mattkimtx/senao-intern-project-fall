from django.db import models

# Create your models here
class log(models.Model):
     ## default
     # id = models.BigAutoField(primary_key=True)
     category = models.CharField(max_length=100)
     subTypeNew = models.CharField(max_length=100)
     eventID = models.CharField(max_length=100)

class device(models.Model):
     