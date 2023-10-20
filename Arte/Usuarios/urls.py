from django.urls import path
# from Usuarios.views import *
from Usuarios import views
from django.contrib.auth.views import LogoutView, LoginView
from .views import UserListView, UserDeleteView




urlpatterns = [
    
    path('login/',LoginView.as_view(template_name="users/login.html"), name="Login"),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"), name="Logout"),
    path('register/',views.register, name="Register"),
    path('edit/',views.edit, name="Edit"),
    path('password/', views.ChangePassword, name="Password"),
    path('crear_usuario/', views.crear_usuario,name="Crear-Usuario"),
    path('usuario_list/', UserListView.as_view(template_name="users/usuario_list.html"), name="Listar-Usuarios"),
     path('usuario_eliminar/<int:pk>',UserDeleteView.as_view(),name="Eliminar-Usuario"),
    

]



