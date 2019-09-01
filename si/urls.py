from django.urls import path

from .views import index, by_planet, RecruitsCreateView

urlpatterns = [
    path('add/', RecruitsCreateView.as_view(), name='add'),
    path('<int:planet_id>/', by_planet, name='by_planet'),
    path('', index, name='index'),
]
