from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.handleLogin,name='handleLogin'),
    path('signup/',views.handleSignup,name='handleSignup'),
    path('logout/',views.handleLogout,name='handleLogout'),
]
