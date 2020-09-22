
from django.urls import path
from .views import register,login,createProfile,viewProfile,logout
urlpatterns = [
    path('login/',login,name='user-login'),
    path('register/',register,name='user-register'),
    path('creatprofile/',createProfile,name='create-profile'),
    path('viewprofile/',viewProfile,name='view-profile'),
    path('logout/',logout,name='user-logout'),
]
