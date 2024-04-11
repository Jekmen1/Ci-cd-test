from django.test import TestCase
from .models import Book
# Create your tests here.
class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title="Book 1", author="giorgi")

        self.assertEqual(book.title,"Book 1")