# Generated by Django 4.2.7 on 2023-12-04 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TbTarefasFat',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('data_atividade', models.DateField()),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('foi_finalizada', models.BooleanField(default=False)),
                ('foi_arquivada', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_tarefas_fat',
                'ordering': ['id'],
            },
        ),
    ]
