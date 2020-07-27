from django.core.management.base import BaseCommand
from pgdjangodemo.models import Profile
import time
import json
import os
module_dir = os.path.dirname(__file__)

class Command(BaseCommand):
    help = 'Method 3'

    def handle(self, *args, **options):
        json_data = open(os.path.join(module_dir, '../', '../', 'fixtures', 'profiles100000.json'))
        profiles = json.load(json_data)
        start_time = time.time()
        ps = []
        for profile in profiles:
            ps.append(Profile(**profile['fields']))
        Profile.objects.bulk_create(ps)
        execution_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS('Done in %s seconds' % execution_time))
