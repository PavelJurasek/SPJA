from django.db import models

# Create your models here.
class Car(models.Model):
    manufacturer = models.CharField(max_length=80)
    model = models.CharField(max_length=50)
    production_year = models.IntegerField(max_length=4)
    consumption = models.FloatField('Consumption per 100 km')
    fuel = models.CharField(max_length=20, default="Diesel")
    odometer_init = models.IntegerField(default=0)

    def __unicode__(self):
        return self.manufacturer +' '+ self.model

class Driver(models.Model):
    name = models.CharField(max_length=120)
    license_since = models.DateField()

    def __unicode__(self):
        return self.name

class Ride(models.Model):
    driver = models.ForeignKey(Driver)
    car = models.ForeignKey(Car)

    initial = models.IntegerField()
    final = models.IntegerField()

    date_start = models.DateField()
    date_end = models.DateField()

    def get_distance(self):
        return self.final - self.initial

    def __unicode__(self):
        return unicode(self.driver) +' on '+ self.date_start.strftime('%d.%m.%Y')

class Refuel(models.Model):
    amount = models.FloatField()
    price = models.FloatField()
    total_price = models.FloatField()
    ride = models.ForeignKey(Ride)

    odometer = models.IntegerField()

    def __unicode__(self):
        return unicode(self.ride.car) +' at '+ str(self.odometer)
