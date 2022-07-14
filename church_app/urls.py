
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views
from django.urls import path , include


app_name = 'church_app'
urlpatterns = [
    path('', views.login_user),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('events', views.events, name='events'),
    path('gallery', views.gallery, name='gallery'),
    path('login_user', views.login_user, name='login'),
    path('gallery/<slug:gallery_slug>', views.gallery, name='gallery_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]