from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from patient.views import PatientListCreateAPIView, PatientRetrieveUpdateDestroyAPIView

app_name = 'patient'
urlpatterns = [
    path('', PatientListCreateAPIView.as_view(), name='api-list'),
    path('delete/<int:id>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
