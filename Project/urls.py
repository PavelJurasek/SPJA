from django.conf.urls import patterns, include, url
from django.contrib import admin

from evidence import views

urlpatterns = patterns('',
    url(r'^$', 'evidence.views.home', name='home'),
    url(r'^drivers$', views.drivers, name='drivers'),
    url(r'^drivers/add$', views.drivers_add, name='add-driver'),
    url(r'^driver/(?P<driver_id>\d+)$', views.driver, name='driver'),
    url(r'^cars$', views.cars, name='cars'),
    url(r'^cars/add', views.cars_add, name='add-car'),
    url(r'^car/(?P<car_id>\d+)$', views.car, name='car'),
    url(r'^ride/(?P<ride_id>\d+)$', views.ride, name='ride'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
