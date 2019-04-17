from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from package.views import PackageRetrieveUpdateDestroyAPIView, PackageListCreateAPIView


app_name = 'package'
urlpatterns = [
    path('', PackageListCreateAPIView.as_view(), name='api-list-create'),
    path('delete/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
