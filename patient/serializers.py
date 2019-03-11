from rest_framework import serializers
from doctor.models import Doctor, Patient


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
