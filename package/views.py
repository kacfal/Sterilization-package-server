from requests import Response, Request
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from package.models import Package
from package.serializers import PackageSerializers


class PackageListCreateAPIView(ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers


class PackageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers
    lookup_field = 'id'
