from django.contrib import admin
from evidence.models import *

class RefuelInline(admin.TabularInline): # StackedInline
    model = Refuel
    extra = 1

class RideAdmin(admin.ModelAdmin):
    inlines = [RefuelInline]

    date_hierarchy = 'date_start'

    fieldsets = [
        ('General', { 'fields': ['car', 'driver'] }),
        ('Odometer', { 'fields': [('initial', 'final')] }),
        ('Date', { 'fields': ['date_start', 'date_end'] })
    ]

    list_display = ('car', 'driver', 'get_distance')

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car', { 'fields': ['manufacturer', 'model', 'production_year'] }),
        ('Engine', { 'fields': ['fuel', 'consumption', 'odometer_init'] })
    ]

class RefuelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', { 'fields': ['ride', 'odometer',] }),
        ('Fuel', { 'fields': ['amount', 'price', 'total_price'] })
    ]

# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(Driver)
admin.site.register(Ride, RideAdmin)
admin.site.register(Refuel, RefuelAdmin)
