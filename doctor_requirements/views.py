from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from doctor_requirements.models import DoctorRequirements
from doctor_requirements.serializers import DoctorRequirementsSerializers


class DoctorRequirementsListCreateAPIView(ListCreateAPIView):
    queryset = DoctorRequirements.objects.all()
    serializer_class = DoctorRequirementsSerializers


class DoctorRequirementsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DoctorRequirements.objects.all()
    serializer_class = DoctorRequirementsSerializers
    lookup_field = 'id'
