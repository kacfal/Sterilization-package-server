from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from doctor.serializers import DoctorSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from package.models import Package
from doctor.models import Doctor


class DoctorListCreateAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers


class DoctorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    lookup_field = 'id'


class DoctorRequirementTools(APIView):

    def get(self, request, **kwargs):
        packages = list(Package.objects.filter(doctor=kwargs['id']).values("package_type"))
        requirements = dict()
        for package in list(packages):
            if package['package_type'] in requirements:
                requirements[package['package_type']] = requirements.get(package['package_type'])+1
            else:
                requirements[package['package_type']] = 1
        _response = dict()
        for k, v in requirements.items():
            _response['Type {}'.format(k)] = {
                'package_type': k,
                'count': v
            }
        return Response(
            _response
        )
