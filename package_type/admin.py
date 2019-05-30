from django.contrib import admin

# Register your models here.
from package_type.models import PackageType

admin.site.register(PackageType)
