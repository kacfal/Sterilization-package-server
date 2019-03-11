from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from patient.models import Patient
from patient.serializers import PatientSerializers


class PatientListCreateAPIView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class PatientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    lookup_field = 'id'

