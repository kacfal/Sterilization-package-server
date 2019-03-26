from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from doctor.models import Doctor
from patient.models import Patient
from package.models import Package
from package.serializers import PackageSerializers


class PackageTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        doctor = Doctor.objects.create(
            name="doctor",
            last_name='doctor',
            office_number=1
        )

        patient = Patient.objects.create(
            name="patient",
            last_name='patient',
        )

        Package.objects.create(
            type_package='Type 3',
            state='Clean',
            doctor=doctor,
            patient=patient
        )

        self.package = Package.objects.create(
            type_package='Type 3',
            state='Clean',
            doctor=doctor,
            patient=patient
        )

        self.valid_payload = {
            "doctor": 1,
            "patient": 1,
            "serialization_data": "2012-09-04 06:00",
            "used_data": "2012-09-04 06:00",
            "type_package": "asaa",
            "state": "Dirty"
        }

        self.invalid_payload = {
        }

    def test_get_list_package(self):
        response = self.client.get(
            reverse('package:api-list-create')
        )
        packages = Package.objects.all()
        serializer = PackageSerializers(packages, many=True)
        self.assertEqual(len(packages), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_get_details_package(self):
        response = self.client.get(
            reverse('package:api-details',
                    kwargs={
                        'id': 1
                    })
        )
        package = Package.objects.first()
        serializer = PackageSerializers(package)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_details_package(self):
        response = self.client.get(
            reverse('package:api-details',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_create_package(self):
        packages = Package.objects.all()
        print(self.valid_payload)
        print("Before: {}".format(len(packages)))
        response = self.client.post(
            reverse('package:api-list-create'),
            data=self.valid_payload,
            format='json'
        )
        print(response)
        packages = Package.objects.all()
        print("After: {}".format(len(packages)))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(packages), 3)

    def test_invalid_create_package(self):
        response = self.client.post(
            reverse('package:api-list-create'),
            data=self.invalid_payload
        )
        packages = Package.objects.all()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(packages), 2)

    def test_valid_delete_package(self):
        response = self.client.delete(
            reverse('package:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        packages = Package.objects.all()
        self.assertEqual(len(packages), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_package(self):
        response = self.client.delete(
            reverse('package:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_package(self):
        response = self.client.put(
            reverse('package:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_package(self):
        response = self.client.put(
            reverse('package:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
