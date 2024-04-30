from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import ActivitiesForm
from .models import Activities
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    activities = Activities.objects.all()
    return render(request, 'home.html', {
        'activities': activities
    })


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # User register
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('activities')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password do not match'
        })

@login_required
def activities(request):
    activity = Activities.objects.all()
    return render(request, 'activities.html', {
        'activity': activity
    })


@login_required
def create_activities(request):

    if request.method == 'GET':
        return render(request, 'create_activities.html', {
            'form': ActivitiesForm
        })
    else:
        try:

            form = ActivitiesForm(request.POST)
            form.save()
            return redirect('activities')
        except ValueError:
            return render(request, 'create_activities.html', {
                'form': ActivitiesForm,
                'error': 'Please provide valida data'
            })
            
@login_required
def activity_detail(request, activity_id):
    if request.method == 'GET':
        activity = get_object_or_404(Activities, pk=activity_id)
        form = ActivitiesForm(instance=activity)
        return render(request, 'activities_detail.html', {'activity': activity, 'form': form})
    else:
        try:
            activity = get_object_or_404(Activities, pk=activity_id)
            form = ActivitiesForm(request.POST, instance=activity)
            form.save()
            return redirect('activities')
        except ValueError:
            return render(request, 'activities_detail.html', {'activity': activity, 'form': form, 'error': 'Error updating task.'})

@login_required
def delete_activities(request, activity_id):
    task = get_object_or_404(Activities, pk=activity_id)
    if request.method == 'POST':
        task.delete()
        return redirect('activities')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('activities')
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
