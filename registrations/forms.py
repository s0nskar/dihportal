from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Proposal, UserProfile

class PartialProposalForm(ModelForm):
	class Meta:
		model = Proposal
		fields = ['title', 'description', 'use', 'thrust']

class ProposalForm(ModelForm):
	class Meta:
		model = Proposal
		fields = []

class UserForm(ModelForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name']

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['roll_no','department', 'year', 'contact']
