from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from doctor.models import Doctor
from package.models import Package
from package.serializers import PackageSerializers
from patient.models import Patient


class PackageListCreateAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers
    lookup_field = 'id'

    # def get_queryset(self):
    #     print(dir(self.request))
    #     # doctor = Doctor.objects.get(id)
    #     patient = Patient.objects.all()
    #     print(self.kwargs)
    #     # print(Package.objects.filter(doctor=self.request.doctor))
        # print(Package.objects.filter(doctor=self.kwargs.get('doctor'), patient=self.kwargs.get('patient')))
        # return Package.objects.filter(doctor=self.request.doctor)


class PackageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers
    lookup_field = 'id'
