from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from doctor_requirements.views import DoctorRequirementsListCreateAPIView, \
    DoctorRequirementsRetrieveUpdateDestroyAPIView

app_name = 'doctor_requirements'
urlpatterns = [
    path('', DoctorRequirementsListCreateAPIView.as_view(), name='api-list-create'),
    path('delete/<int:id>/', DoctorRequirementsRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', DoctorRequirementsRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', DoctorRequirementsRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
