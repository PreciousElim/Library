from django.shortcuts import render
from .models import Loan
from rest_framework import permissions, generics
from .serializers import LoanSerializers
from .permissions import IsBorrowerOrReadOnly


class LoanView(generics.ListCreateAPIView):
    serializer_class = LoanSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Loan.objects.filter(borrower=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(borrower=self.request.user)
    
    
class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializers
    permission_classes = [permissions.IsAuthenticated, IsBorrowerOrReadOnly]
    

# Create your views here.
