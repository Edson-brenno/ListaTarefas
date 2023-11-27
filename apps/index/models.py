from django.db import models

# Create your models here.

class TbTarefasFat(models.Model):

    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    data_criacao = models.DateField(auto_now_add=True, blank=False, null=False)
    foi_finalizada = models.BooleanField(default=False)
    foi_arquivada = models.BooleanField(default=False)

    class Meta:
        
        ordering = ['id']

        db_table = 'tb_tarefas_fat'
        