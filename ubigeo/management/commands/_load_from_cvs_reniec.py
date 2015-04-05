"""
Load ubigeo with columns ITEM UBIGEO Departamento Provincia Distrito from CSV
"""

import csv

from ubigeo.models import Ubigeo

def load_from_csv(path):
    cur_reg, cur_prov, cur_dist = ('', '', '')
    name = ''
    parent = None
    with open(path, 'rb') as csvfile:
        document = csv.reader(csvfile, delimiter=',')
        for row in document:
            if cur_reg != row[3]:
                name = cur_reg = row[3]
                parent = set_ubigeo(name, '%s0000' % row[0], Ubigeo.POLITICAL_DIVISION_CHOICES.REGION)
                print u'Load %s' % name
            if cur_prov != row[4]:
                name = cur_prov = row[4]
                if parent.political_division == Ubigeo.POLITICAL_DIVISION_CHOICES.PROVINCE:
                    parent = parent.parent
                parent = set_ubigeo(name, '%s00' % ''.join((row[0], row[1])), Ubigeo.POLITICAL_DIVISION_CHOICES.PROVINCE, parent)
            if cur_dist != row[5]:
                name = cur_dist = row[5]
                set_ubigeo(name, '%s' % ''.join((row[0], row[1], row[2])), Ubigeo.POLITICAL_DIVISION_CHOICES.DISTRICT, parent)

def set_ubigeo(name, reniec, political_division, parent=None):
    u = dict(
        name=name.title(),
        reniec_code=reniec,
        political_division=political_division,
        parent=parent
    )
    ubigeo = Ubigeo(**u)
    ubigeo.save()
    return ubigeo
