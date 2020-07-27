from django.core.management.base import BaseCommand
from pgdjangodemo.models import Profile
import time
import json
import os
module_dir = os.path.dirname(__file__)

class Command(BaseCommand):
    help = 'Generate'

    def handle(self, *args, **options):
        start_time = time.time()
        json_data = open(os.path.join(module_dir, '../', '../', 'fixtures', 'profiles1000.json'))
        profiles = json.load(json_data)
        all_profiles = []
        i = 1
        for page in range(100):
            for profile in profiles:
                profile['pk'] = 1
                i += 1
                all_profiles.append(profile)
        with open(os.path.join(module_dir, '../', '../', 'fixtures', 'profiles100000.json'), 'w') as outfile:
            json.dump(all_profiles, outfile)
        execution_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS('Done in %s seconds' % execution_time))
