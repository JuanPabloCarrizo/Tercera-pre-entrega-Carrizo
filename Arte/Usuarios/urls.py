from django.urls import path
# from Usuarios.views import *
from Usuarios import views
from django.contrib.auth.views import LogoutView, LoginView



urlpatterns = [
    
    path('login/',LoginView.as_view(template_name="users/login.html"), name="Login"),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"), name="Logout"),
    path('register/',views.register, name="Register"),
    path('edit/',views.edit, name="Edit"),
    path('password/', views.ChangePassword, name="Password"),

]



