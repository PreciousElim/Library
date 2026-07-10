from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.urls import reverse
from django.contrib.auth import get_user_model


class BookAPITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'testing',
            password = "testing123"
        )
        self.client.force_authenticate(user=self.user)
        self.book = Book.objects.create(
            title = "Test Book",
            author = "Test Author",
            isbn="1111111111",
            published_date="2020-01-01",
            is_available=True,            
        )       
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_book(self):
        url = reverse("book-list")
        data = {
            "title" : "New Book",
            "author" : "New Author",
            "isbn" : "2222222222",
            "published_date" : "2002-09-10",
            "is_available" : True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        
        
    def test_unauthenticated_create_fails(self):
        client = APIClient()
        url = reverse("book-list")
        data = {
            "title" : "Sneaky Book",
            "author" : "Nobody",
            "isbn" : "3333333333",
            "published_date" : "2021-02-06",
            "is_available" : True,
        }
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

