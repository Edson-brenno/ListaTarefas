from django.urls import path
from apps.registrar_usuario.views import registro_usuario

urlpatterns = [
    path('registrar/', registro_usuario),
]