from django.urls import path
from .views import CreateAccount
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', CreateAccount.as_view(), name = 'create-user'),
    path('sign-in/',obtain_auth_token, name = 'sign-in' )
]


