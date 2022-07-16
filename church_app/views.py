from multiprocessing import context
from re import template
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from . forms import contactusForm
from .models import Gallery
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, loginForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('church_app:login')
    else:
        form = UserRegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])    
            return redirect('church_app:home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('church_app:login')
    else:
        form = loginForm()
    context = {'form': form}
      
    return render(request, 'authentication/login.html', context)


@login_required()
def profile(request):
    return render(request, 'profile.html')


def home(request):
    template = 'index.html'
    return render(request, template) 

def about(request):
    template='about.html'
    return render(request, template)



def events(request):
    template='events.html'
    return render(request, template)



def contacts(request):
    if request.method == 'POST':
        form = contactusForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = contactusForm

    template = 'contacts.html'
    context = {'form':form}
    return render(request, template, context)

def gallery(request, gallery_slug=None):
    template='gallery.html'
    thumbnail = None
    pictures = Gallery.objects.all()
    if gallery_slug != None:
        thumbnail = get_object_or_404(Gallery, slug=gallery_slug)
        
    pictures = Gallery.objects.filter(slug=gallery_slug)
    context = {'pictures':pictures, 'thumbnail':thumbnail}
    return render(request, template, context)

   