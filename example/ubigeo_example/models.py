# -*- coding: utf-8 -*-

from django.db import models
from ubigeo.models import Ubigeo

class Incident(models.Model):
    location = models.ForeignKey(Ubigeo,
                                 related_name='location',
                                 blank=True,
                                 null=True, )

    def __unicode__(self):
        return "id: %s | location: %s" % (self.pk, self.location)
