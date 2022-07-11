from multiprocessing import context
from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import contactusForm
from .models import Contactus, Gallery
from django. contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST': 
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
            
         else:
            messages. success(request,("There was an Error in Logging in, Try Again... "))
            return redirect('login')
   
    else:    
        return render(request, 'authenticate/login.html',{} )



def home(request):
    template = 'index.html'
    return render(request, template) 

def about(request):
    template='about.html'
    return render(request, template)

def teaching(request):
    template='teaching.html'
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

def gallery(request):
    template='gallery.html'
    pictures = Gallery.objects.all()


    return render(request, template)
        