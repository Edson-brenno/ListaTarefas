from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from index.models import TbTarefasFat

# Create your views here.
@login_required(login_url='/login/')
def index(request):

    if request.method == 'POST':
        
        titulo_tarefa = request.POST.get('titulo_tarefa','')
        dt_tarefa = datetime.strptime(request.POST.get('dt_tarefa',''),'%Y-%m-%d' )

        TbTarefasFat.adicionar_tarefa(titulo_tarefa, dt_tarefa, request.user)

        return redirect('/index/')

    return render(request, 'to_do/to_do.html', context={'usuario':request.user.username, 
                                                        'tarefas_ativas':TbTarefasFat.obter_tarefas_ativas(request.user),
                                                        'tarefas_finalizadas':TbTarefasFat.obter_tarefas_finalizadas(request.user)})

@login_required(login_url='/login/')
def finalizar_tarefa(request):

    if request.method == 'POST':

        id = request.POST.get('id',)

        TbTarefasFat.finalizar_tarefa(id)

        return redirect('/index/')
    
@login_required(login_url='/login/')
def retomar_tarefa(request):

    if request.method == 'POST':

        id = request.POST.get('id',)

        TbTarefasFat.retomar_tarefa(id)

        return redirect('/index/')