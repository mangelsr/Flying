# Generated by Django 2.0 on 2017-12-26 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airlineID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('iata', models.CharField(blank=True, max_length=5, null=True)),
                ('icao', models.CharField(blank=True, max_length=5, null=True)),
                ('callsign', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airportID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('iata', models.CharField(blank=True, max_length=5, null=True)),
                ('icao', models.CharField(blank=True, max_length=5, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('alt', models.FloatField(blank=True, null=True)),
                ('timezone', models.IntegerField(blank=True, null=True)),
                ('dst', models.CharField(blank=True, max_length=5, null=True)),
                ('tz_db', models.CharField(blank=True, max_length=150, null=True)),
                ('tipe', models.CharField(blank=True, max_length=25, null=True)),
                ('source', models.CharField(blank=True, max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('iso1', models.CharField(blank=True, max_length=5, null=True)),
                ('iso2', models.CharField(blank=True, max_length=5, null=True)),
                ('campo', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(blank=True, max_length=5, null=True)),
                ('sAirport', models.CharField(blank=True, max_length=5, null=True)),
                ('dAirport', models.CharField(blank=True, max_length=5, null=True)),
                ('codeshare', models.CharField(blank=True, max_length=5, null=True)),
                ('stops', models.IntegerField(blank=True, null=True)),
                ('equipment', models.CharField(blank=True, max_length=100, null=True)),
                ('airlineID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Flying.Airline')),
                ('dAirportID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Flying.Airport')),
                ('sAirportID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Flying.Airport')),
            ],
        ),
    ]
