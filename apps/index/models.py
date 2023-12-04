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
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        
        ordering = ['id']

        db_table = 'tb_tarefas_fat'
        