from django import forms

class Form(forms.Form):
    origen = forms.CharField()
    destino = forms.CharField()
    directo = forms.ChoiceField(widget=forms.RadioSelect())
    escala = forms.ChoiceField(widget=forms.RadioSelect())