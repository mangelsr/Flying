from django import forms

from pymongo import MongoClient
from bson.objectid import ObjectId

class Form(forms.Form):
	client = MongoClient('mongodb://miguel:12345@ds245277.mlab.com:45277/flying')
	db = client.flying
	
	paises = db.countries.distinct('name')
	PAISES = []
	for pais in paises:
		tup = pais, pais
		PAISES.append(tup)
		
	# PAISES = ver_paises()
	CHOICES = (('directo','Vuelo directo'),('escala','Vuelo con escalas'))
	origen = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	destino = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	# radio = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, label='')
