
__all__=['county_data','stores_data','roads_data','towns_data']

from django.shortcuts import render
from django.http import HttpResponse
from .models import Counties,Stores,Towns,Roads
from django.views.generic import TemplateView
from django.core.serializers import serialize
import datetime
from django.utils.timezone import utc

def Gisbi_home(request):
    today= datetime.datetime.utcnow().date()
    return render(request, 'index.html',{"today" :today})
class Gisbi_stores(TemplateView):
    template_name='stores.html'
class Gisbi_stories(TemplateView):
    template_name='storymaps.html'
class Gisbi_three(TemplateView):
    template_name='threedmaps.html'

def county_data(request):
    c_data=serialize('geojson',Counties.objects.all())
    return HttpResponse(c_data,content_type='json')
def stores_data(request):
    st_data=serialize('geojson',Stores.objects.all())
    return HttpResponse(st_data,content_type='json')
def towns_data(request):
    tw_data=serialize('geojson',Towns.objects.all())
    return HttpResponse(tw_data,content_type='json')
def roads_data(request):
    rd_data=serialize('geojson',Roads.objects.all())
    return HttpResponse(rd_data,content_type='json')

#Define a geo-fence,Nairobi is the fence
def geo_fence(request):
    fence=Counties.objects.get(county='Nairobi')
    nai=fence.geom.geojson
    return HttpResponse(nai,content_type='json')
