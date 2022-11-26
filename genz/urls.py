from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='first-page'),
    path('home/', homePage, name='home'),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerPage, name="register"),
]

