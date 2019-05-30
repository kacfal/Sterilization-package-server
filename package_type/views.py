from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from package_type.models import PackageType
from package_type.serializers import PackageTypeSerializers


class PackageTypeListCreateAPIView(ListCreateAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeSerializers


class PackageTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeSerializers
    lookup_field = 'id'
