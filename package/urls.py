from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from doctor.views import DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView

app_name = 'doctor'
urlpatterns = [
    path('', DoctorListCreateAPIView.as_view(), name='api-list'),
    path('delete/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
