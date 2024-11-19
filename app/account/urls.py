
from django.urls import path
from .views import UserCreateApiView, UserDetailApiView, change_password, reset_password

urlpatterns = [
    path('users/', UserCreateApiView.as_view()),
    path('details/', UserDetailApiView.as_view()),
    path('change-password/', change_password, name='change_password'),
    path('reset-password/', reset_password, name='reset_password'),
]
