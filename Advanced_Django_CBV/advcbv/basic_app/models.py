from django.db import models

# Create your models here.
# Note that django sets an 'id' field as primary key
# if no primary key field is specified.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name
