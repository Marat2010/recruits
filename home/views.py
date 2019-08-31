from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Recruits
from .models import Planets
from .forms import RecruitsForm


class RecruitsCreateView(CreateView):
    template_name = 'home/create.html'
    form_class = RecruitsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planets'] = Planets.objects.all()
        return context


def by_planet(request, planet_id):
    recrs = Recruits.objects.filter(planet=planet_id)
    planets = Planets.objects.all()
    current_planet = Planets.objects.get(pk=planet_id)
    context = {'recrs': recrs, 'planets': planets, 'current_planet': current_planet}
    return render(request, 'home/by_planet.html', context)


def index(request):
    recrs = Recruits.objects.all()
    planets = Planets.objects.all()
    context = {'recrs': recrs, 'planets': planets}
    return render(request, 'home/index.html', context)




