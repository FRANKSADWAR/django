from __future__ import unicode_literals
from django.db import models
from django.db.models import Manager as GeoManager
from django.conf.locale.en import formats as en_formats
en_formats.DATETIME_FORMAT = "d b Y H:i:s"
from django.contrib.gis.db import models as gis_models

from django.db import models
from django.contrib.gis.db import models as gis_models


class Counties(models.Model):
    objectid = models.IntegerField()
    county = models.CharField(max_length=20)
    geom = gis_models.MultiPolygonField(srid=4326)
    class Meta:
        verbose_name_plural="Counties"
    def __repr__(self):
        return '[County: %s,object_id: %s]' % (self.county,self.objectid)

class Stores(models.Model):
    store = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    latitude = models.CharField(max_length=80)
    longitude = models.CharField(max_length=80)
    geom = gis_models.MultiPointField(srid=4326)
    class Meta:
        verbose_name_plural="Distribution Centers"
    def __repr__(self):
        return '[Store: %s,Address: %s]' % (self.store,self.address)

class Towns(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    ktowns_field = models.BigIntegerField()
    ktowns_id = models.BigIntegerField()
    town_name = models.CharField(max_length=20)
    geom = gis_models.MultiPointField(srid=4326)
    class Meta:
        verbose_name_plural="Kenya Towns"
    def __repr__(self):
        return '[Town: %s,Area: %f]' % (self.town_name,self.area)

class Roads(models.Model):
    fnode_field = models.BigIntegerField()
    tnode_field = models.BigIntegerField()
    lpoly_field = models.BigIntegerField()
    rpoly_field = models.BigIntegerField()
    length = models.FloatField()
    kenroad_field = models.BigIntegerField()
    kenroad_id = models.BigIntegerField()
    geom = gis_models.MultiLineStringField(srid=4326)
    class Meta:
        verbose_name_plural="Roads"


