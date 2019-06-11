from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from doctor.views import DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView, DoctorRequirementTools

app_name = 'doctor'
urlpatterns = [
    path('', DoctorListCreateAPIView.as_view(), name='api-list-create'),
    path('delete/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-delete'),
    path('details/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-details'),
    path('update/<int:id>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='api-update'),
    path('<int:id>/requirements/', DoctorRequirementTools.as_view(), name='requirements')

]

urlpatterns = format_suffix_patterns(urlpatterns)
