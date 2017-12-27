import time

from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect

from .forms import Form
from .models import *


def cargar_paises():
	Country.objects.all().delete()
	f = open('countries.dat', 'r')
	for line in f:
		line = line.replace('\\N', '')
		line = line.replace('"', '')
		line = line.split(',')
		try:
			pais = Country.objects.create(
				name = line[0],
				iso1 = line[1],
				iso2 = line[2],
				campo = line[3].replace('\n',''),
			)
		except:
			pass
	f.close()


def cargar_aerolineas():
	Airline.objects.all().delete()
	f = open('airlines.dat', 'r')
	for line in f:
		line = line.replace('\\N', '')
		line = line.replace('"', '')
		line = line.split(',')
		try:
			aerolinea = Airline.objects.create(
				airlineID = int(line[0]),
				name = line[1],
				alias = line[2],
				iata = line[3],
				icao = line[4],
				callsign = line[5],
				country = line[6],
				active = line[7].replace('\n','')
			)
		except:
			pass
	f.close()

def cargar_aeropuertos():
	Airport.objects.all().delete()
	f = open('airports.dat', 'r')
	for line in f:
		line = line.replace('\\N', '')
		line = line.replace('"', '')
		line = line.split(',')
		try:
			aeropuerto = Airport.objects.create(
				airportID = int(line[0]),
				name = line[1],
				city = line[2],
				country = line[3],
				iata = line[4],
				icao = line[5],
				lat = line[6],
				lon = line[7],
				alt = line[8],
				timezone = int(line[9]),
				dst = line[10],
				tz_db = line[11],
				tipe = line[12],
				source = line[13].replace('\n', '')
			)		
		except:
			pass
	f.close()

def cargar_rutas():
	Route.objects.all().delete()
	f = open('routes.dat', 'r')
	for line in f:
		line = line.replace('\\N', '')
		line = line.replace('"', '')
		line = line.split(',')
		try:
			ruta = Route.objects.create(
				airline = line[0],
				airlineID = Airline.objects.get(airlineID=int(line[1])),
				sAirport = line[2],
				sAirportID = Airport.objects.get(airportID=int(line[3])),
				dAirport = line[4],
				dAirportID = Airport.objects.get(airportID=int(line[5])),
				codeshare = line[6],
				stops = int(line[7]),
				equipment = line[8].replace('\n', '')
			)
		except:
			pass
	f.close()


@require_http_methods(['GET'])
def index(request):
	form = Form()
	return render(request,'formulario.html', {'form': form})

@csrf_protect
@require_http_methods(['POST'])
def buscar(request):
	start = time.time()
	
	pais_origen = request.POST['origen']
	pais_destino = request.POST['destino']
	n_escalas = request.POST['tipo']
	
	aeropuertos_origen = list(Airport.objects.filter(country=pais_origen))
	aeropuertos_destino = list(Airport.objects.filter(country=pais_destino))
	
	routes = Route.objects.filter(
		sAirportID__in = aeropuertos_origen,
		dAirportID__in = aeropuertos_destino,
		stops = n_escalas
	)

	rutas = []
	for r in routes:
		try:
			ruta = {}
			ruta['aerolinea'] = r.airlineID.name
			ruta['aero_origen'] = r.sAirportID.name
			ruta['aero_destino'] = r.dAirportID.name
			ruta['paradas'] = r.stops
			rutas.append(ruta)
		except:
			pass
	
	end = time.time()

	print(end - start)
	
	return JsonResponse(rutas, safe=False)

def cargar_base(request):
	cargar_paises()
	cargar_aerolineas()
	cargar_aeropuertos()
	cargar_rutas()
	return HttpResponse('ok')
