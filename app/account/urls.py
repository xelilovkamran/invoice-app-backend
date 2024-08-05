
from django.urls import path
from .views import UserCreateApiView, UserDetailApiView

urlpatterns = [
    path('users/', UserCreateApiView.as_view()),
    path('details/', UserDetailApiView.as_view()),
]
