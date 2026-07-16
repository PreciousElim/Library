from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, status
from rest_framework.response import Response


User = get_user_model()
class CreateAccount (generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
            
    
    def create (self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception = True)
        serializers.save()
        
        return Response({
            'message' : 'Account created sucessfully.'},
            status = status.HTTP_201_CREATED
        )

# Create your views here.
