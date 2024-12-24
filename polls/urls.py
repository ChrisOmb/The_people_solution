from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
   
    path('about/', views.about, name='about'),
    path('', views.landing_page, name="landing" ),
    path("home/", views.home, name ="home"),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('create/', views.create_poll, name='create_poll'),

]

