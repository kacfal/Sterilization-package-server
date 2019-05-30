from django.db import models

# Create your models here.
from doctor.models import Doctor
from package_type.models import PackageType


class DoctorRequirements(models.Model):
    """
    TODO: Count of item
    """
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    package_type = models.ManyToManyField(PackageType)
    count = models.PositiveIntegerField()
