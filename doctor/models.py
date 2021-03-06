from django.core.validators import MinValueValidator
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    office_number = models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)

    def __unicode__(self):
        return f'{self.id}. {self.name} {self.last_name}'

    def __str__(self):
        return f'{self.id}. {self.name} {self.last_name}'
