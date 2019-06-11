from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from package.views import PackageRetrieveUpdateDestroyAPIView, PackageListAPIView, PackageCreateAPIView


app_name = 'package'
urlpatterns = [
    path('', PackageListAPIView.as_view(), name='api-list'),
    path('create/', PackageCreateAPIView.as_view(), name='api-create'),
    path('delete/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
