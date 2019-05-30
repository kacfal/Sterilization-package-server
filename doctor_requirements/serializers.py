from rest_framework import serializers
from doctor_requirements.models import DoctorRequirements


class DoctorRequirementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorRequirements
        fields = '__all__'
