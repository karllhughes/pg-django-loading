import time
import os
module_dir = os.path.dirname(__file__)
from django.core.management.commands.loaddata import Command as BaseCommand

class Command(BaseCommand):
    def handle(self, *fixture_labels, **options):
        start_time = time.time()
        super(Command, self).handle(*fixture_labels, **options)
        execution_time = time.time() - start_time
        self.stdout.write(self.style.SUCCESS('Done in %s seconds' % execution_time))
