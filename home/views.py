from django.shortcuts import render

# Create your views here.
def home (request):
	return render(request, 'app/inicio.html')

def proyectos (request):
	return render(request, 'app/proyectos.html')
