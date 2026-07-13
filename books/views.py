from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagination
from django_filters.rest_framework import DjangoFilterBackend



# class BookView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
    
#     def post(self,request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
# class BookDetailView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         books = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(books)
#         return Response(serializer.data)   
    
#     def put(self, request,pk):
#         books = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(books, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     def patch(self,request,pk):
#         books = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(books, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         books = get_object_or_404(Book, pk=pk)
#         books.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = BookPagination
    filterset_fields = ['author', 'is_available', 'title']
    
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = BookPagination
    filterset_fields = ['author', 'is_available', 'title']
    
    