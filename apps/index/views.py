from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):

    return render(request, 'to_do/to_do.html', context={'usuario':request.user.username})
