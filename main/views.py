from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout
from django.http import HttpRequest
from django.urls import reverse_lazy

from .forms import *
from .models import *
from .utils import *


def index(requests):
    return render(requests, 'main/index.html')


def second_title(requests):
    tasks = Task.objects.order_by("-id")
    return render(requests, 'main/second_title.html', {'title': "Задачи", 'tasks': tasks})


def about_us(requests):
    return render(requests, 'main/about_us.html')


def create_task(requests):
    error = ""
    if requests.method == "POST":
        form = TaskForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('second')
        else:
            error = "Форма была неверной"

    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(requests, 'main/create_task.html', context)


def profile(requests):
    return render(requests, 'main/profile.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect("login")
