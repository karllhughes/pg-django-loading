from django.core.management.base import BaseCommand
from pgdjangodemo.models import Profile
import time
import json
import os
from django.db import transaction
module_dir = os.path.dirname(__file__)

class Command(BaseCommand):
    help = 'Method 1a'

    def handle(self, *args, **options):
        start_time = time.time()
        json_data = open(os.path.join(module_dir, '../', '../', 'fixtures', 'profiles100000.json'))
        profiles = json.load(json_data)
        with transaction.atomic():
            for profile in profiles:
                p = Profile(**profile['fields'])
                p.save()
        execution_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS('Done in %s seconds' % execution_time))
