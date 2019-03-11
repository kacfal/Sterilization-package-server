from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from doctor.models import Doctor
from doctor.serializers import DoctorSerializers


class DoctorListCreateAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers


class DoctorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    lookup_field = 'id'
