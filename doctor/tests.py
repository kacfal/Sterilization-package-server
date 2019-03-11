from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from doctor.models import Doctor, Patient
from doctor.serializers import DoctorSerializers, PatientSerializers


# Create your tests here.
class DoctorTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        Doctor.objects.create(
            name="test1",
            last_name='test1',
            office_number=1
        )

        self.doctor = Doctor.objects.create(
            name="test2",
            last_name='test2',
            office_number=2
        )

        self.valid_payload = {
            "name": "test",
            "last_name": 'test',
            "office_number": "10"
        }

        self.invalid_payload = {}

    def test_get_list_doctor(self):
        response = self.client.get(
            reverse('doctor:api-list')
        )
        doctors = Doctor.objects.all()
        serializer = DoctorSerializers(doctors, many=True)
        self.assertEqual(len(doctors), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_get_details_doctor(self):
        response = self.client.get(
            reverse('doctor:api-details',
                    kwargs={
                        'id': 1
                    })
        )
        doctor = Doctor.objects.first()
        serializer = DoctorSerializers(doctor)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_details_doctor(self):
        response = self.client.get(
            reverse('doctor:api-details',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_create_doctor(self):
        response = self.client.post(
            reverse('doctor:api-list'),
            data=self.valid_payload
        )
        doctors = Doctor.objects.all()
        self.assertEqual(len(doctors), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_doctor(self):
        response = self.client.post(
            reverse('doctor:api-list'),
            data=self.invalid_payload
        )
        doctors = Doctor.objects.all()
        self.assertEqual(len(doctors), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_doctor(self):
        response = self.client.delete(
            reverse('doctor:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        doctors = Doctor.objects.all()
        self.assertEqual(len(doctors), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_doctor(self):
        response = self.client.delete(
            reverse('doctor:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        doctors = Doctor.objects.all()
        self.assertEqual(len(doctors), 2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_doctor(self):
        response = self.client.put(
            reverse('doctor:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_doctor(self):
        response = self.client.put(
            reverse('doctor:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PatientTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        Patient.objects.create(
            name="test1",
            last_name='test1',
        )

        self.Patient = Patient.objects.create(
            name="test2",
            last_name='test2',
        )

        self.valid_payload = {
            "name": "test",
            "last_name": 'test'
        }

        self.invalid_payload = {}

    def test_get_list_patient(self):
        response = self.client.get(
            reverse('patient:api-list')
        )
        patients = Patient.objects.all()
        serializer = PatientSerializers(patients, many=True)
        self.assertEqual(len(patients), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_get_details_patient(self):
        response = self.client.get(
            reverse('patient:api-details',
                    kwargs={
                        'id': 1
                    })
        )
        patient = Patient.objects.first()
        serializer = PatientSerializers(patient)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_details_patient(self):
        response = self.client.get(
            reverse('patient:api-details',
                    kwargs={
                        'id': 0
                    })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_create_patient(self):
        response = self.client.post(
            reverse('patient:api-list'),
            data=self.valid_payload
        )
        patients = Patient.objects.all()
        self.assertEqual(len(patients), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_patient(self):
        response = self.client.post(
            reverse('patient:api-list'),
            data=self.invalid_payload
        )
        patients = Patient.objects.all()
        self.assertEqual(len(patients), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_patient(self):
        response = self.client.delete(
            reverse('patient:api-delete',
                    kwargs={
                        'id': 1
                    })
        )
        patients = Patient.objects.all()
        self.assertEqual(len(patients), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_patient(self):
        response = self.client.delete(
            reverse('patient:api-delete',
                    kwargs={
                        'id': 0
                    })
        )
        patients = Patient.objects.all()
        self.assertEqual(len(patients), 2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_patient(self):
        response = self.client.put(
            reverse('patient:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_patient(self):
        response = self.client.put(
            reverse('patient:api-update',
                    kwargs={
                        'id': 1
                    }),
            data=self.invalid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)