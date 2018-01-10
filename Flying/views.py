import time

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_ajax.decorators import ajax

from pymongo import MongoClient
from bson.objectid import ObjectId

from .forms import Form
from .models import *


client = MongoClient('locamongodb://miguel:12345@ds245277.mlab.com:45277/flyinglhost')
db = client.flying


@require_http_methods(['GET'])
def index(request):
	form = Form()
	return render(request,'formulario.html', {'form': form})


@ajax
@require_http_methods(['POST'])
def buscar(request):
	start = time.time()

	paises = db.countries.distinct('name')

	origen = request.POST['origen']
	destino = request.POST['destino']
	stops = int(request.POST['tipo'])	

	aeropuertos_origen = db.airports.find({'country': origen}, {'airportID': 1})
	aeropuertos_destino = db.airports.find({'country': destino}, {'airportID': 1})
	
	aero_origen = []
	for r in aeropuertos_origen:
		aero_origen.append(r.get('airportID'))

	aero_destino = []
	for r in aeropuertos_destino:
		aero_destino.append(r.get('airportID'))
	
	routes = db.routes.find({'sAirportID': {"$in": aero_origen}, 
							'dAirportID': {"$in": aero_destino}, 
							'stops': stops})

	rutas = []
	for r in routes:
		try: 
			ruta = {}
			ruta['aerolinea'] = db.airlines.find_one({'airlineID': r['airlineID']}, {'name': 1})['name']
			ruta['aero_origen'] = db.airports.find_one({'airportID': r['sAirportID']}, {'name': 1})['name']
			ruta['aero_destino'] = db.airports.find_one({'airportID': r['dAirportID']}, {'name': 1})['name']
			ruta['paradas'] = r['stops']
			rutas.append(ruta)
		except:
			pass
		
	end = time.time()
	
	print(end - start)

	if len(rutas) > 0:
		return render(request, 'table.html', {'rutas': rutas})
	else:
		return render(request, 'no_result.html')
