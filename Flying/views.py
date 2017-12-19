from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Form


def cargarAerolineas():
	aerolineas = {}
	f = open('airlines.dat', 'r')
	for line in f:
		line = line.split(',')
		aerolineas[line[0]] = {'nombre': line[1].replace('"', ''), 
			'iata': line[3].replace('"', ''), 'pais': line[6].replace('"', '')}
	f.close()
	return aerolineas

def cargarAeropuertos():
	airports = {}
	f = open('airports.dat', 'r')
	for line in f:
		line = line.split(',')
		if line[3].replace('"', '') not in airports:
			airports[line[3].replace('"', '')] = [line[0]]
		else:
			airports[line[3].replace('"', '')].append(line[0])
	f.close()
	return airports

def cargarResultados(origen, destino):
	airports = cargarAeropuertos()

	source_airports = airports[origen]
	destination_airport = airports[destino]

	airlines_id = set()
	f = open('routes.dat', 'r')
	for line in f:
		line = line.split(',')
		if (line[3] in source_airports) and (line[5] in destination_airport):
			airlines_id.add(line[1])
	f.close()

	airlines = cargarAerolineas()

	resultados = []
	for air_id in airlines_id:
		resultados.append(airlines[air_id])

	return resultados


def index(request):
	if request.method == 'POST':
		context = {}
		form = Form(request.POST)
		if form.is_valid():
			origen = request.POST.get('origen')
			destino = request.POST.get('destino')
			context['form'] = form
			context['lista_resultados'] = cargarResultados(origen, destino)
		return render(request, 'formulario.html', context)
	elif request.method == 'GET':
		form = Form()
		return render(request,'formulario.html', {'form': form})
	else:
		return HttpResponse('Metodo no soportado')
		