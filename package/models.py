from django.db import models
from doctor.models import Doctor
from package_type.models import PackageType
from patient.models import Patient


class Package(models.Model):
    STATE_OF_TOOL = (
        ('Clean', 'Clean'),
        ('Dirty', 'Dirty')
    )
    package_type = models.OneToOneField(PackageType, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True)
    state = models.TextField(default='Dirty', choices=STATE_OF_TOOL)
    used_data = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    serialization_data = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return f'{self.package_type}'

    def __str__(self):
        return f'{self.package_type}'
