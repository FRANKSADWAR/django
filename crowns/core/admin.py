from django.contrib import admin
from .models import Counties,Stores,Roads,Towns
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

class StoresAdmin(OSMGeoAdmin):
    list_display=('store','address')
    serch_fields=('store','address')
    filter_fields=('store','address')
class CountyAdmin(OSMGeoAdmin):
    list_display = ('county','objectid')
    search_fields = ('county','objectid')
    filter_fields=('county','objectid')
class TownsAdmin(OSMGeoAdmin):
    list_display = ('town_name','area')
    search_fields = ('town_name','area')
    filter_fields=('town_name','area')
class RoadsAdmin(OSMGeoAdmin):
    list_display=('kenroad_id','length')
    search_fields=('kenroad_id','length')
    filter_fields=('kenroad_id','length')

admin.site.register(Stores,StoresAdmin)
admin.site.register(Counties,CountyAdmin)
admin.site.register(Towns,TownsAdmin)
admin.site.register(Roads,RoadsAdmin)
