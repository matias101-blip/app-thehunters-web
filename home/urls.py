from django.urls import path 
from . views import home, proyectos

urlpatterns = [
            path('', home, name="home"),
            path('Proyectos/', proyectos, name="proyectos")
]
