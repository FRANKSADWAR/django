from django.urls import path

from djgeojson.views import GeoJSONLayerView 
from django.conf.urls import url
from .views import Gisbi_home,Gisbi_stores,Gisbi_stories,Gisbi_three,stores_data,county_data,roads_data,towns_data,geo_fence

from django.conf import settings


urlpatterns=[
    url(r'^$',Gisbi_home,name='home'),
    url(r'stories/',Gisbi_stories.as_view(),name='stories'),
    path('stores/',Gisbi_stores.as_view(),name='stores'),
    path('threedmaps/',Gisbi_three.as_view(),name='3DMaps'),
    path('county/',county_data,name='county'),
    path('crownstores/',stores_data,name='crownstores'),
    path('roads/',roads_data,name='roads'),
    path('towns/',towns_data,name='towns'),
    path('virtual_fence/',geo_fence,name='virtual_fence'),

]