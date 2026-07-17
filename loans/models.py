from django.db import models
from books.models import Book
from django.conf import settings


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name ='loans')
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="loans")
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.book.title} borrowed by {self.lender.username}"
    
# Create your models here.
