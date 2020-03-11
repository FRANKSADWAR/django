import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties,Stores,Towns,Roads

#Counties Mapping
counties_mapping = {
    'objectid': 'OBJECTID',
    'county': 'COUNTY',
    'geom': 'MULTIPOLYGON',
}
county_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'data','County.shp'),)
def crun(verbose=True):
    lm=LayerMapping(Counties,county_shp,counties_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)


#Stores Mapping
stores_mapping = {
    'store': 'STORE',
    'address': 'Address',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT',
}
store_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'data','crowndata.shp'),)
def srun(verbose=True):
    lm=LayerMapping(Stores,store_shp,stores_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)

#Towns Mapping
towns_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'ktowns_field': 'KTOWNS_',
    'ktowns_id': 'KTOWNS_ID',
    'town_name': 'TOWN_NAME',
    'geom': 'MULTIPOINT',
}
towns_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'data','majortowns.shp'),)
def trun(verbose=True):
    lm=LayerMapping(Towns,towns_shp,towns_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)

#Roads Mapping
roads_mapping = {
    'fnode_field': 'FNODE_',
    'tnode_field': 'TNODE_',
    'lpoly_field': 'LPOLY_',
    'rpoly_field': 'RPOLY_',
    'length': 'LENGTH',
    'kenroad_field': 'KENROAD_',
    'kenroad_id': 'KENROAD_ID',
    'geom': 'MULTILINESTRING',
}
roads_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'data','ken_roads.shp'),)
def run(verbose=True):
    lm=LayerMapping(Roads,roads_shp,roads_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)
