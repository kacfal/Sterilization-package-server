from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from package.models import Package
from package.serializers import PackageSerializers, PackageSerializersGet


class PackageListAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializersGet


class PackageCreateAPIView(CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers


class PackageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializers
    lookup_field = 'id'
