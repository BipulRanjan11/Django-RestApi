from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Work(models.Model):
    YOUTUBE='YT'
    INSTAGRAM='IG'
    OTHER='OT'
    WORK_TYPE_CHOICES=[(YOUTUBE,'Youtube'),(INSTAGRAM,'Instagram'),(OTHER,'Other'),]
    link=models.URLField()
    work_type=models.CharField(max_length=2,choices=WORK_TYPE_CHOICES,default=OTHER,)
    artist=models.ManyToManyField('Artist')

    def __str__(self):
        return f'{self.get_work_type_display()}-{self.link}'
