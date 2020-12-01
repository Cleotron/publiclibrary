from django.test import TestCase
from pl.models import Book
from django.test import Client

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(author="pepe", title="libro1", in_use= False, reservations= 0)
        Book.objects.create(author="pipo", title="libro2", in_use= True, reservations= 2)
        Book.objects.create(author="pupu", title="libro3", in_use= True, reservations= 0)

    def test_included_books(self):
        response = self.client.get("/")
        self.assertContains(response, "libro1", html=True)
        self.assertContains(response, "libro2", html=True)
        self.assertContains(response, "libro3", html=True)

