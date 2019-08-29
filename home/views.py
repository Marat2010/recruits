from django.shortcuts import render

from .models import Recruits


def index(request):
    recr = Recruits.objects.all()
    return render(request, 'home/index.html', {'recr': recr})



