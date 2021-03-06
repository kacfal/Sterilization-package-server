from django.db import models

# Create your models here.
from doctor.models import Doctor
from package_type.models import PackageType


class DoctorRequirements(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __unicode__(self):
        return f'{self.doctor}' f'{self.package_type}'  f'{ self.count}'

    def __str__(self):
        return f'{self.doctor}' f'{self.package_type}'  f'{ self.count}'