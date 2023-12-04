from django.shortcuts import render, HttpResponse
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

    return render(request, 'to_do/to_do.html', context={'usuario':request.user.username, 'tarefas':TbTarefasFat.obter_tarefas_ativas(request.user)})
