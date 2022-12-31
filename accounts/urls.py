from django.urls import path
from . import views

urlpatterns = [
    #login, logout
    path('entrar/', views.entrar, name="entrar"), 
    path('sair/', views.sair, name="sair"),

    #minha conta
    path('meu_perfil/', views.meu_perfil, name="meu_perfil"),

    #dados da secretaria
    path('cadastrar_secretaria/', views.cadastrar_secretaria, name="cadastrar_secretaria"),
    
    #dados do medico
    path('cadastrar_medico/', views.cadastrar_medico, name="cadastrar_medico"),
    
    #dados do paciente
    path('registrar/', views.cadastrar_paciente, name="cadastrar_paciente"),

    #dados de todos
    path('users/', views.users, name="users"),
]