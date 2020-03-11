
import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties,Stores,Towns,Roads

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
