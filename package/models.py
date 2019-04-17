from django.db import models
from doctor.models import Doctor
from patient.models import Patient


class Package(models.Model):
    STATE_OF_TOOL = (
        ('Clean', 'Clean'),
        ('Dirty', 'Dirty')
    )
    created = models.DateTimeField(auto_now=True)
    serialization_data = models.DateTimeField(blank=True, null=True)
    used_data = models.DateTimeField(blank=True, null=True)
    type_package = models.CharField(max_length=120)
    state = models.TextField(default='Dirty', choices=STATE_OF_TOOL)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True)
