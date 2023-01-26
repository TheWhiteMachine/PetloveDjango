from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/', views.post),
    path('login/', views.loginPage),
    path('registro/', views.registerPage),
    path('registro_mascota/', views.pet),
    path('coment/', views.coment),
    path('logout/', views.logoutPage),
    path('post/<int:id>', views.post)
]
