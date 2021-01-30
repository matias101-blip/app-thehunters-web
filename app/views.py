from django.shortcuts import render

# Create your views here.
def hello (request):
	return render(request, 'app/hello.html')

def memes (request):
	return render(request, 'app/memes.html')
