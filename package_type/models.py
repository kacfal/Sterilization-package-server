from django.db import models


class PackageType(models.Model):
    package_name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=120)

    def __unicode__(self):
        return f'{self.package_name}'

    def __str__(self):
        return f'{self.package_name}'
