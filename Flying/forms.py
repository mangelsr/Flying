from django import forms

class Form(forms.Form):
	def ver_paises():
		paises = []
		f = open('countries.dat', 'r')
		for line in f:
			line = line.split(',')
			paises.append((line[0], line[0]))
		f.close()
		return paises
		
	PAISES = ver_paises()
	CHOICES = (('directo','Vuelo directo'),('escala','Vuelo con escalas'))
	origen = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	destino = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PAISES)
	# radio = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, label='')
