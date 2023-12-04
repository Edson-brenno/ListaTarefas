from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def login(request):

    mensagem = ""

    if request.method == 'POST':

        usuario_form = request.POST.get('usuario','') 
        senha_form = request.POST.get('senha','')
        
        # Verifica a autenticidade do usuário
        usuario = authenticate(request, username=usuario_form, password=senha_form)

        if usuario is not None:
            
            auth_login(request, usuario)

            return redirect('/index/')
        else:
            mensagem = ("usuario ou senha inválidos")
    
    
    return render(request, 'login/login.html', context={'mensagem':mensagem})
   

def logout(request):

    auth_logout(request)

    return redirect('/login/')