from django.contrib import admin

# Register your models here.
from package.models import Package


class PackageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_package', 'created']
    list_display_links = ['id', 'type_package']
    list_filter = ['type_package', 'doctor', 'state']

    class Meta:
        model = Package


admin.site.register(Package, PackageModelAdmin)
