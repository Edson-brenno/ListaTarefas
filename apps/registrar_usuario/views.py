from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# Create your views here.
def registro_usuario(request):

    if request.method == 'POST':
        
        usuario = request.POST.get('username',None)
        senha = request.POST.get('senha',None)

        if usuario != None and senha != None:

            user = User.objects.create_user(username=usuario, password=senha)

            user.save()
            
        return render(request,'registro/registrar.html', context={})
    else:
        
        return render(request,'registro/registrar.html', context={})