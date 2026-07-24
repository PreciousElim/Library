from rest_framework import serializers
from .models import Loan

class LoanSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = ['id','book', 'borrower', 'borrowed_date', 'returned_date', 'is_returned']
        read_only_fields = ['borrower', 'borrowed_date', 'returned_date', 'is_returned']
    