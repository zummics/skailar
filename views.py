from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *

from .forms import PostForm, CustomUserCreationForm, ProfileForm, UserForm
from .filters import PostFilter

from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, '404.html')
    else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def abuse(request):
    return render(request, 'abuse.html')

def domain(request):
    return render(request, 'domains.html')

def gameservers(request):
    return render(request, 'game-servers.html')

def handler404(request, *args, **argv):
    response = render('404.html')
    response.status_code = 404
    return response

def contact(request):
    return render(request, 'contact.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, 'register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def terms(request):
    return render(request, 'terms.html')