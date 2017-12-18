from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	if request.method == 'GET':
		return render(request, 'formulario.html')
	elif request.method == 'POST':
		#TODO logica del query
		context = {}
		return render(request, 'formulario.html', context)
	else:
		return HttpResponse('Metodo no soportado', content_type='text/plain; charset=utf8')