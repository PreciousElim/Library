from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Loan

@receiver(post_save, sender=Loan)
def update_book_availability(sender, instance, created, **kwargs):
    book = instance.book
    if created:
        book.is_available = False
    elif instance.is_returned:
        book.is_available = True
    else:
        book.is_available = False
    book.save()
    
    
@receiver(post_delete, sender=Loan)
def make_book_available_on_delete(sender, instance, **kwargs):
    book = instance.book
    book.is_available = True
    book.save()
    