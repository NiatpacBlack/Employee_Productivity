from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks', views.second_title, name='second'),
    path('about_us', views.about_us, name='about'),
    path('create_task', views.create_task, name='create'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
]