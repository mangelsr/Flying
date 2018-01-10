from django import forms

from pymongo import MongoClient
from bson.objectid import ObjectId

class Form(forms.Form):
	"""def ver_paises():
		paises = []
		f = open('countries.dat', 'r')
		for line in f:
			line = line.split(',')
			paises.append((line[0], line[0]))
		f.close()
		return paises"""

	client = MongoClient('localhost', 27017)
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
