from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20
    
    def get_paginated_response(self, data):
        return Response({
            'books_count': self.page.paginator.count,
            'previous_page': self.get_previous_link(),
            'next_page': self.get_next_link(),
            'books': data
        })