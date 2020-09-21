
from django.urls import path
from .views import register,login,createProfile,viewProfile
urlpatterns = [
    path('login/',login,name='user-login'),
    path('register/',register,name='user-register'),
    path('creatprofile/',createProfile,name='create-profile'),
    path('viewprofile/',viewProfile,name='view-profile'),
]
