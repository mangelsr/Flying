from django import forms

class Form(forms.Form):
	def verPaises():
		paises = []
		f = open("countries.dat","r")
		for line in f:
			pais = line.split(",")[0]
			paises.append(pais)
		f.close()
		return paises
		
	PAISES = verPaises()
	CHOICES = (('directo','Vuelo directo'),('escala','Vuelo con escalas'))
	origen = forms.CharField(widget=forms.Select(), choices=PAISES)
	destino = forms.CharField(widget=forms.Select(), choices=PAISES)
	radio = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, label='')

	

