from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __unicode__(self):
        return f'{self.id}. {self.name} {self.last_name}'

    def __str__(self):
        return f'{self.id}. {self.name} {self.last_name}'

