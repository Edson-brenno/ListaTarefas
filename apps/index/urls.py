from django.urls import path
from apps.index.views import index,finalizar_tarefa, retomar_tarefa

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('finalizar_tarefa/',finalizar_tarefa),
    path('retomar_tarefa/', retomar_tarefa),
]
