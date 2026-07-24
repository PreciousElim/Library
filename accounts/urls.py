from django.urls import path
from .views import CreateAccount, LogOut

urlpatterns = [
    path('register/', CreateAccount.as_view(), name = 'create-user'),
    path('logout/', LogOut.as_view(), name = 'logout')
]


