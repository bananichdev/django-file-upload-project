from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from .models import File


class FileAPITestCase(APITestCase):
    def test_upload_file(self):
        url = '/upload/'
        file_content = b'Test'
        uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        response = self.client.post(url, {'file': uploaded_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)
        uploaded_file = File.objects.first()
        self.assertEqual(uploaded_file.file.read(), file_content)

    def test_list_files(self):
        File.objects.create(file='./test.txt')
        url = '/files/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
