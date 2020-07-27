from django.core.management.base import BaseCommand
from pgdjangodemo.models import Profile
import time
import os
module_dir = os.path.dirname(__file__)

class Command(BaseCommand):
    help = 'Method 4'

    def handle(self, *args, **options):
        start_time = time.time()
        data = Profile.objects.from_csv(os.path.join(module_dir, '../', '../', 'fixtures', 'profiles1000.csv'))
        execution_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS('Done in %s seconds' % execution_time))
