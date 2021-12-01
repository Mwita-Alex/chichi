from django.urls import path
from .import views

urlpatterns = [
     path('login', views.login, name = "login"),
     path('register', views.register, name = "register"),
     path('logout', views.logout, name = "logout"),
     path('dashboard', views.dashboard, name = "dashboard"),
     path('downloadpdfform', views.downloadpdfform, name = "downloadpdfform"),
     path('pdfgenerator', views.pdfgenerator, name = "pdfgenerator"),
     path('reset', views.reset, name = "reset"),
    
]
