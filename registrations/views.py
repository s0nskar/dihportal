from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import *

import requests
import json

def check_token_validity(id_token):
	if id_token:
		payload = {'id_token': id_token}
		res = requests.get(
				'https://www.googleapis.com/oauth2/v3/tokeninfo',
				params=payload
			)
		if res.status_code == requests.codes.ok:
			json_data = json.loads(res.text)
			return json_data

def index(request):
	return render(request, 'home.html', {})

def callback(request):
	if request.method == 'POST':
		id_token = request.POST.get('id_token')
		data = check_token_validity(id_token)
		if data:
			user_id = data['sub']
			try:
				u = User.objects.get(username=user_id)
			except:
				email = data['email']
				first_name = data['given_name']
				last_name = data['family_name']
				u = User.objects.create_user(
						user_id,
						email=email,
						first_name=first_name,
						last_name=last_name
					)
			u.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, u)
			return JsonResponse({'success': True})
		return JsonResponse({'error': 'Login token is not valid'})

@login_required
def dashboard(request):
	context = {}
	try:
		proposal = Proposal.objects.get(user=request.user)
		context['proposal'] = proposal
	except:
		pass
	return render(request, 'dashboard.html', context)

@login_required
def proposal(request):
	if request.method == "POST":
		try:
			proposal = Proposal.objects.get(user=request.user)
			form = PartialProposalForm(request.POST, instance=proposal)
		except:
			form = PartialProposalForm(request.POST)
		if form.is_valid():
			proposal = form.save(commit=False)
			proposal.user = request.user
			proposal.save()
		else:
			print form.errors
		return dashboard(request)
	else:
		try:
			proposal = Proposal.objects.get(user=request.user)
			form = PartialProposalForm(instance=proposal)
		except:
			form = PartialProposalForm()
		# form.fields['title'].widget.attrs['readonly'] = True
		return render(request, 'proposal.html', {'form': form})

@login_required
def profile(request):
	if request.method == "POST":
		# Getting user profile instance and passing it into form
		profile = UserProfile.objects.get(user=request.user)
		profile_form = UserProfileForm(request.POST, instance=profile)
		if profile_form.is_valid():
			profile = profile_form.save(commit=True)
			return dashboard(request)
		else:
			print form.errors   # TODO: Show errors
	else:
		user = request.user
		try:
			profile = UserProfile.objects.get(user=user)
		except:
			profile = UserProfile.objects.create(user=user)
		user_form = UserForm(instance=user)
		profile_form = UserProfileForm(instance=profile)  # TODO: Disable fields

		# Disabling fields
		user_form.fields['email'].widget.attrs['readonly'] = True
		user_form.fields['first_name'].widget.attrs['readonly'] = True
		user_form.fields['last_name'].widget.attrs['readonly'] = True

		return render(request, 'profile.html', {'user_form':user_form,\
				'profile_form': profile_form})

# def user(request):
#     User.objects.create_superuser('dihadmin', 'sanskarmodi97@gmail.com', 'password')
#     return HttpResponse("Made")
