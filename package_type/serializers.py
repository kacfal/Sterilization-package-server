from rest_framework import serializers

from package_type.models import PackageType


class PackageTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = PackageType
        fields = '__all__'
