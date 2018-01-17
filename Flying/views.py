import time
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django_ajax.decorators import ajax

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

from .forms import Form
from .models import *


client = MongoClient('mongodb://miguel:12345@ds245277.mlab.com:45277/flying')
db = client.flying

ENTIDADES = ['countries', 'airlines', 'airports', 'routes']

@require_http_methods(['GET'])
def lista(request, table):
	if table not in ENTIDADES:
		return HttpResponse(dumps({'detalle': 'Modelo no existe'}), content_type='application/json', status=404)
	
	lista = db[table].find()
	return HttpResponse(dumps(lista), content_type='application/json')

@csrf_exempt
@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def modelo(request, table, id):
	if table not in ENTIDADES:
		return HttpResponse(dumps({'detalle': 'Modelo no existe'}), content_type='application/json', status=404)
	
	if table == 'countries':
		id_field = 'name'
	elif table == 'airlines':
		id_field = 'airlineID'
		id = int(id)
	elif table == 'airports':
		id_field = 'airportID'
		id = int(id)
	elif table == 'routes':
		id_field = 'airlineID'

	busqueda = db[table].find({id_field: id})

	if request.method == 'GET':
		if busqueda.count() == 0: 
			return HttpResponse(dumps({'detalle': 'No encontrado'}), content_type='application/json', status=404)
		else:
			return HttpResponse(dumps(busqueda), content_type='application/json')
	
	elif request.method == 'POST':
		if busqueda.count() > 0: 
			return HttpResponse(dumps({'detalle': 'Metodo "POST" no permitido'}), content_type='application/json', status=405)
		else:
			body = json.loads(request.body.decode('utf-8'))
			db[table].insert_one(body)
			return HttpResponse(dumps(body), content_type='application/json')
			
	elif request.method == 'PUT':
		if busqueda.count() == 0: 
			return HttpResponse(dumps({'detalle': 'No encontrado'}), content_type='application/json', status=404)
		elif busqueda.count() > 1: 
			return HttpResponse(dumps({'detalle': 'Metodo "PUT" no permitido'}), content_type='application/json', status=405)
		else:
			body = json.loads(request.body.decode('utf-8'))
			db[table].replace_one({id_field: id}, body)
			return HttpResponse(dumps(body), content_type='application/json')
	
	elif request.method == 'DELETE':
		if busqueda.count() == 0: 
			return HttpResponse(dumps({'detalle': 'No encontrado'}), content_type='application/json', status=404)
		elif busqueda.count() > 1: 
			return HttpResponse(dumps({'detalle': 'Metodo "DELETE" no permitido'}), content_type='application/json', status=405)
		else:
			db[table].delete_one({id_field: id})
			return HttpResponse(status=204)
		

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
