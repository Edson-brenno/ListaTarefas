from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def login(request):

    mensagem = ""

    usuario_form = request.POST.get('usuario','') 
    senha_form = request.POST.get('senha','')
    
    if request.method == 'POST':
        
        # Verifica a autenticidade do usuário
        usuario = authenticate(request, username=usuario_form, password=senha_form)

        if usuario is not None:
            
            auth_login(request, usuario)

            return redirect('/index/')

        print(usuario_form)
        if usuario is None:

            mensagem = ("usuario ou senha inválidos")

            return render(request, 'login/login.html', context={'mensagem': mensagem,'usuario':usuario_form,'senha2':senha_form})
        
    
    
    return render(request, 'login/login.html', context={'mensagem':mensagem,'usuario':usuario_form,'senha2':senha_form})
   

def logout(request):

    auth_logout(request)

    return redirect('/login/')