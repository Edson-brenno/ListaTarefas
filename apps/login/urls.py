from django.urls import path
from apps.login.views import login,logout

urlpatterns = [
    path('login/', login),
    path('logout/',logout)
]
