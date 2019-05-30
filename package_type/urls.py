from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from package_type.views import PackageTypeListCreateAPIView, PackageTypeRetrieveUpdateDestroyAPIView

app_name = 'package_type'
urlpatterns = [
    path('', PackageTypeListCreateAPIView.as_view(), name='api-list-create'),
    path('delete/<int:id>/', PackageTypeRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', PackageTypeRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', PackageTypeRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
