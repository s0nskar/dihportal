from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    summer_course = models.CharField(max_length=5)
    mentor = models.CharField(max_length=50)
    mentor_department = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    team = models.ManyToManyField(Student)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title