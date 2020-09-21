
from django.urls import path
from .views import register,login
urlpatterns = [
    path('login/',login,name='user-login'),
    path('register/',register,name='user-register'),
]
