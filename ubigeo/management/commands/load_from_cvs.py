from django.core.management.base import BaseCommand
from django.utils import translation

from _load_from_cvs_reniec import load_from_csv


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        translation.activate('es')
        load_from_csv('/home/micky/Development/django-ubigeo-peru/docs/ubigeos.csv')
        self.stdout.write('Successfully')
        translation.deactivate()
