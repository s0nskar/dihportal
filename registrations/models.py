from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	roll_no = models.CharField(max_length=15)
	year = models.CharField(max_length=5)
	contact = models.CharField(max_length=15)
	department = models.CharField(max_length=50)

	def __unicode__(self):
		return "%s %s" %(self.user.first_name, self.user.last_name)

class Proposal(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	description = models.TextField()
	use = models.TextField()
	thrust = models.CharField(max_length=30)
	util = models.CommaSeparatedIntegerField(max_length=5)
	submitted = models.DateTimeField(auto_now_add=True)
	approved = models.NullBooleanField()

	def __unicode__(self):
		return self.title
