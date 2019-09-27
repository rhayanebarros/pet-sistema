from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

@login_required
def home(request):
    contadorCadastro = Usuario.objects.count()    
    return render(request, 'home.html', {'count': contadorCadastro})

# @login_required
# def home2(request):
#     contadorUsuarios = User.objects.count()
#     return render(request, 'home.html', {'count': contadorUsuarios})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def form(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'form.html', {'form': form})

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário/Senha inválido. Tente novamente.')
    return redirect('home')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

class Cadastro(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro.html'