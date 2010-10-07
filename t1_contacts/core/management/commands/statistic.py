from django.core.management.base import BaseCommand, CommandError
from django.db import models

class Command(BaseCommand):
    args = ''
    help = 'List of models and items in each models'

    def handle(self, *args, **options):
        for model in models.get_models():
            #self.stdout.write('Model "%s" - %d items' % (model,models.objects.count()))
            print ('Model "%s" - %d items' % (model,model.objects.count()))

