from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse

from .models import Bunk, User
from django.template import loader 
from django.utils import timezone


# main bunks page?
# should show all bunks. 
# add images (in HTML??)
def index(request):
	bunks_list = Bunk.objects.order_by('-bunk_time')
	users_list = User.objects.order_by('-username') # ?
	context = {
		'bunks_list': bunks_list,
		'users_list': users_list,
	}
	return render(request, 'bunks/index.html', context)

	# output = ''
	# for b in bunks_list:
	# 	# do the bunker, bunkee, and then the representation
	# 	output += b.__str__()
	# 	output += '\n \n'
	# return HttpResponse(output)

# personal bunk feed for a user
def detail(request, username):
	u = get_object_or_404(User, username=username)
	incoming = Bunk.objects.filter(to_user=u).order_by('-bunk_time')
	outgoing = Bunk.objects.filter(from_user=u).order_by('-bunk_time')
	context = {
		'u': u,
		'incoming': incoming,
		'outgoing': outgoing,
	}
	# do incoming for u
	# do outgoing for u
	return render(request, 'bunks/detail.html', context)

# bunking form for a user
def makeBunk(request, username):
	if request.method == 'POST':
		# if there was a request made it should get the user sent
		# should this be get object or 404
		bunkee = User.objects.get(username=request.POST['username'])
		bunker = User.objects.get(username=username)
		newBunk = Bunk(from_user=bunker, to_user=bunkee, bunk_time=timezone.now())
		newBunk.save()

		# redirect to existing detail page
		return redirect('bunks:detail', username)
		
	else:
		# no post request
		other_users = User.objects.exclude(username=username)
		u = get_object_or_404(User, username=username)
		context = {
			'u': u,
			'other_users': other_users
		}
		return render(request, 'bunks/makeBunk.html', context)