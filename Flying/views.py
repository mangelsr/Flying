from django.shortcuts import render, redirect
from django.http import HttpResponse


def verVuelos(request):
	if request.method == "POST":
		form = Form(request.POST)
		if form.is_valid():
			vuelos = form.save(commit=False)
			vuelos.save()
		return redirect('formulario.html')
	elif request.method == "GET":
		form = Form()
		return render(request,'formulario.html', {'form':form})
		