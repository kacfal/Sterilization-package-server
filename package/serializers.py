from rest_framework import serializers

from package.models import Package


class PackageSerializersGet(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'
        depth = 2


class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
