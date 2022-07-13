
from django.urls import path
from .import views
from django.urls import path , include

app_name = 'church_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('events', views.events, name='events'),
    path('gallery', views.gallery, name='gallery'),
    path('login_user', views.login_user, name='login'),
    path('gallery/<slug:gallery_slug>', views.gallery, name='gallery_detail'),
]