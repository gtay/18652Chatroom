from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from chatroom.models import *

import datetime

@login_required
def home(request):
    all_messages = Message.objects.all()
    return render(request, 'htmlfiles/home.html', {'messages':all_messages})

@login_required
def send_message(request):
    errors = []
    
    if not 'message' in request.POST or not request.POST['message']:
        errors.append('You must enter a message to send!')
    else:
        new_message = Message(text=request.POST['message'], time_stamp=datetime.datetime.now(), name=request.user.username)
        new_message.save()

    messages = Message.objects.all()
    context = {'messages':messages, 'errors':errors}
    return render(request, 'htmlfiles/home.html', context)

def register(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'htmlfiles/register.html', context)

    errors = []
    context['errors'] = errors

    if not 'username' in request.POST or not request.POST['username']:
        errors.append('Name is required.')
    else:
        context['username'] = request.POST['username']

    if not 'password1' in request.POST or not request.POST['password1']:
        errors.append('Password is required.')
    if not 'password2' in request.POST or not request.POST['password2']:
        errors.append('Password is required.')

    if 'password1' in request.POST and 'password2' in request.POST \
    and request.POST['password1'] and request.POST['password2'] \
    and request.POST['password1'] != request.POST['password2']:
        errors.append('Passwords did not match.')

    if len(User.objects.filter(username = request.POST['username'])) > 0:
        errors.append('That name is already taken.')

    if errors:
        return render(request, 'htmlfiles/register.html', context)

    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password1'])
    new_user.save()

    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(request, new_user)
    return redirect('/chatroom/')