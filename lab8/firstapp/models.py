from django.db import models


class Teacher (models.Model):
    record = models.IntegerField(primary_key='true')
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    secondName = models.CharField(max_length=25)
    birthday = models.DateField('my date')
    telephone = models.CharField(max_length=11)
    experience = models.IntegerField()
    genger_choices=[('M','Man'),('W','Woman')]
    gender = models.CharField(max_length=2,choices=genger_choices,default='M')
    discipline = models.CharField(max_length=25)
def __str__(self):
    return self.field_name
