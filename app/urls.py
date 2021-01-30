from django.urls import path
from . views import hello, memes

urlpatterns = [
    path('hola/', hello, name="hello" ),
    path('memes/', memes, name="memes"),
]
