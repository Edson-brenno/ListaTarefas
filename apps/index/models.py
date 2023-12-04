from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TbTarefasFat(models.Model):

    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    data_atividade = models.DateField(blank=False, null=False)
    data_criacao = models.DateField(auto_now_add=True, blank=False, null=False)
    foi_finalizada = models.BooleanField(default=False)
    foi_arquivada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    # Adiciona uma tarefa no models
    @classmethod
    def adicionar_tarefa(cls, titulo, data, usuario):

        nova_tarefa = cls(titulo= titulo, data_atividade = data, usuario = usuario)
        nova_tarefa.save()
    
    # Obter atividades ativas
    @classmethod
    def obter_tarefas_ativas(cls,usuario):

        return cls.objects.filter(usuario=usuario, foi_finalizada=False).values('id','titulo','data_atividade','data_criacao',
                                                                                'foi_finalizada').order_by('data_atividade')

    # Obter atividades Finalizadas
    @classmethod
    def obter_tarefas_finalizadas(cls,usuario):

        return cls.objects.filter(usuario=usuario, foi_finalizada=True).values('id','titulo','data_atividade','data_criacao',
                                                                                'foi_finalizada').order_by('data_atividade')
    
    # Finaliza uma tarefa
    @classmethod
    def finalizar_tarefa(cls,id):
        tarefa = cls.objects.get(id=id)
        tarefa.foi_finalizada = True
        tarefa.save()

    # Retoma uma tarefa
    @classmethod
    def retomar_tarefa(cls,id):
        tarefa = cls.objects.get(id=id)
        tarefa.foi_finalizada = False
        tarefa.save()
    class Meta:
        
        ordering = ['id']

        db_table = 'tb_tarefas_fat'
        