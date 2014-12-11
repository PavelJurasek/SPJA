from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime

from evidence.models import Driver, Car, Ride

# Create your views here.
def home(request):
    return render(request, 'evidence/home.html', {})

def drivers(request):
    return render(request, 'evidence/drivers.html', {
        'drivers': Driver.objects.all()
    })

def drivers_add(request):
    try:
        Driver.objects.get(name=request.POST['name'])

        return render(request, 'evidence/drivers.html', {
            'drivers': Driver.objects.all(),
            'error_message': 'Driver with name '+ request.POST['name'] +' already exists.',
        })
    except Driver.DoesNotExist:
        d = Driver(name=request.POST['name'], license_since=request.POST['date'])
        d.save()

    return HttpResponseRedirect(reverse('drivers'))


def driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    dist = 0
    for ride in driver.ride_set.all():
        dist += ride.get_distance()

    return render(request, 'evidence/driver.html', {
        'driver': driver,
        'odometer': dist
    })

def cars(request):
    return render(request, 'evidence/cars.html', {
        'cars': Car.objects.all()
    })

def cars_add(request):
    try:
        c = Car.objects.get(manufacturer=request.POST['manufacturer'], model=request.POST['model'])

        return render(request, 'evidence/cars_add.html', {
            'cars': Car.objects.all(),
            'error_message': 'Car '+ unicode(c) +' already exists.',
        })
    except Car.DoesNotExist:
        c = Car(manufacturer=request.POST['manufacturer'], model=request.POST['model'])
        c.production_year = int(request.POST['production_year'][:4])
        c.consumption = request.POST['consumption']
        c.fuel = request.POST['fuel']
        c.odometer_init = request.POST['odometer_init']
        c.save()

        return HttpResponseRedirect(reverse('cars'))
    except KeyError:
        pass

    return render(request, 'evidence/cars_add.html', {})

def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    try:
        latest_ride = car.ride_set.latest('date_end')
    except Ride.DoesNotExist:
        latest_ride = Ride(final=0)

    print(request.POST)
    try:
        r = Ride()
        r.car = car
        r.driver = Driver.objects.get(pk=request.POST['driver'])
        r.initial = request.POST['initial'] if 'initial' in request.POST else latest_ride.final
        r.final = request.POST['final']
        r.date_start = datetime.strptime(request.POST['start'], '%Y-%m-%d')
        r.date_end = datetime.strptime(request.POST['end'], '%Y-%m-%d')

        r.save()

        return HttpResponseRedirect(reverse('car', args=(car_id)))

    except KeyError:
        pass

    return render(request, 'evidence/car.html', {
        'car': car,
        'rides': car.ride_set.all().order_by('date_start'),
        'drivers': Driver.objects.all(),
        'today': datetime.now(),
        'latest_ride': latest_ride,
        'distance': latest_ride.final - car.odometer_init if latest_ride else 0,
    })

def ride(request, ride_id):
    ride = get_object_or_404(Ride, pk=ride_id)
    return render(request, 'evidence/ride.html', {
        'ride': ride
    })
