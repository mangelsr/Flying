from django.db import models

# Create your models here.
class Airport(models.Model):
    airportID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    iata = models.CharField(max_length=5, blank=True, null=True)
    icao = models.CharField(max_length=5, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    timezone = models.IntegerField(blank=True, null=True)
    dst = models.CharField(max_length=5, blank=True, null=True)
    tz_db = models.CharField(max_length=150, blank=True, null=True)
    tipe = models.CharField(max_length=25, blank=True, null=True)
    source = models.CharField(max_length=75, blank=True, null=True)


class Airline(models.Model):
    airlineID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    iata = models.CharField(max_length=5, blank=True, null=True)
    icao = models.CharField(max_length=5, blank=True, null=True)
    callsign = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=5, blank=True, null=True)


class Route(models.Model):
    airline = models.CharField(max_length=5, blank=True, null=True)
    airlineID = models.ForeignKey('Airline', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    sAirport = models.CharField(max_length=5, blank=True, null=True)
    sAirportID = models.ForeignKey('Airport', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    dAirport = models.CharField(max_length=5, blank=True, null=True)
    dAirportID = models.ForeignKey('Airport', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    codeshare = models.CharField(max_length=5, blank=True, null=True)
    stops = models.IntegerField(blank=True, null=True)
    equipment = models.CharField(max_length=100, blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=75, primary_key=True)
    iso1 = models.CharField(max_length=5, blank=True, null=True)
    iso2 = models.CharField(max_length=5, blank=True, null=True)
    campo = models.CharField(max_length=5, blank=True, null=True)
