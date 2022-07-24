
from django.contrib.auth import views as auth_views
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
    path('gallery/<slug:gallery_slug>', views.gallery, name='gallery_detail'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/',views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
]