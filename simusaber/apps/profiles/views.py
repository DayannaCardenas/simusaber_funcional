from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.profiles.form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def user_validate_group(roles=[]):
	def decorator(view_func):
		def arguments(request, *args, **kwargs):
			if request.user.groups.exists():
				if request.user.groups.all()[0].name in roles:
					return view_func(request, *args, **kwargs)
			return redirect('profiles:login')
		return arguments
	return decorator

def login_user(request):
    context={}
    if request.POST:
        form=AuthenticationForm(None, request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profiles:home')
            else:
                form.add_error(None, "Usuario no encontrado")
        context['form']=form
    return render(request, "general/login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/profiles/login')

@login_required(login_url='/profiles/login')
# @user_validate_group(roles=['Administrator', 'Authorizer'])
def home_view(request):
    return render(request, "general/home.html")
