from django.urls import path
from apps.index.views import index

urlpatterns = [
    path('', index),
]
