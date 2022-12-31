from django.http import HttpResponse
from django.shortcuts import render
from .models import Users
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404

@has_permission_decorator('cadastrar_secretaria')
def users(request):
    if request.method == 'GET':
        secretarias = Users.objects.filter(cargo="S")
        medicos = Users.objects.filter(cargo="M")
        pacientes = Users.objects.filter(cargo="P")
        context = {
        'secretarias': secretarias,
        'medicos': medicos,
        'pacientes': pacientes,
    }
        return render(request, 'accounts/users.html', context)

#login, logout, meuPerfil, attPerfil
def entrar(request):
    if request.method == 'GET':
            if request.user.is_authenticated:
                return render(request, 'home.html')
            return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('Usuario invalido')

        auth.login(request, user)
        return HttpResponse('Usuario logado')

def sair(request):
    request.session.flush()
    return redirect(reverse('entrar'))

def meu_perfil(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/meu_perfil.html', context)

#secretaria
@has_permission_decorator('cadastrar_secretaria')
def cadastrar_secretaria(request):
    if request.method == 'GET':
        return render(request, 'accounts/cadastrar_secretaria.html')
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('ERRO')

        user = Users.objects.create_user(first_name=name, username=email, email=email, password=password, cargo="S",)
        return HttpResponse('conta criada')



#medico
@has_permission_decorator('cadastrar_medico')
def cadastrar_medico(request):
    if request.method == 'GET':
        medicos = Users.objects.filter(cargo="M")
        return render(request, 'accounts/cadastrar_medico.html', {'medicos': medicos})
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('ERRO')

        user = Users.objects.create_user(first_name=name, username=email, email=email, password=password, cargo="M",)
        return HttpResponse('conta criada')

#paciente
def cadastrar_paciente(request):
    if request.method == 'GET':
        return render(request, 'accounts/cadastrar_paciente.html')
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('ERRO')

        user = Users.objects.create_user(first_name=name, username=email, email=email, password=password, cargo="P",)
        return HttpResponse('conta criada')