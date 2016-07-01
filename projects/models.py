from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    summer_course = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, null=True)
    team = models.ManyToManyField(Student)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    plan_first_second = models.TextField()
    plan_third_fourth = models.TextField()
    plan_fifth_sixth = models.TextField()
    plan_seventh_eight = models.TextField()
    plan_after_eight = models.TextField(null=True, blank=True)
    team_leader = models.ForeignKey(Student, null=True, related_name="project_team_leader")

    def __unicode__(self):
        return self.title

class Panel(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, blank=True)

    def __unicode__(self):
        return self.name
