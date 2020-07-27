from django.db import models
from postgres_copy import CopyManager


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    objects = CopyManager()

    def save(self, *args, **kwargs):
        if self.name:
            self.first_name, self.last_name = self.name.split(" ", 1)
        super(Profile, self).save(*args, **kwargs)
