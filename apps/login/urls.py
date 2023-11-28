from django.urls import path
from apps.login.views import login

urlpatterns = [
    path('login/', login),
]
