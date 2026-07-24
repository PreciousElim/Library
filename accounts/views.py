from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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
        
class LogOut(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'message': 'Logged out successfully'},
                status = status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response ({
                'error': 'Invalid Token'},
                status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
