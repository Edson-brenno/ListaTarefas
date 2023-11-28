from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# Create your views here.
def registro_usuario(request):

    if request.method == 'POST':

        # Variaveis fomulario 
        usuario = request.POST.get('username',None)
        senha = request.POST.get('senha',None)
            
        # Verica se o usuário existe
        if User.objects.filter(username = usuario).exists():

            mensagem_error = "usuario já existe"

            return render(request,'registro/registrar.html', context={"mensagem":mensagem_error})
            
        else:

            user = User.objects.create_user(username=usuario, password=senha)

            user.save()

            mensagem_error = "Usuario Criado"
            
            return redirect('/login/')
    
    else:
        
        return render(request,'registro/registrar.html', context={"mensagem":'O Usuario e senha não podem ser nulo'})