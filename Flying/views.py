from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method == 'GET':
		return redner('formulario.html')
	elif request.method == 'POST':
		#TODO logica del query
		context = {}
		return render('formulario.html', context)
	else
		return httpresponse('Metodo no soportado')