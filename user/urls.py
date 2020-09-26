
from django.urls import path
from .views import register,login,createProfile,viewProfile,logout,searchlist,viewProfilewithID
urlpatterns = [
    path('login/',login,name='user-login'),
    path('register/',register,name='user-register'),
    path('creatprofile/',createProfile,name='create-profile'),
    path('viewprofile/',viewProfile,name='view-profile'),
    path('logout/',logout,name='user-logout'),
    path('searchlist/',searchlist,name='user-list'),
    path('viewprofile/<int:pk>/',viewProfilewithID,name='view-profile-id'),
]
