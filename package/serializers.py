from rest_framework import serializers

from package.models import Package


class PackageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'
