
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('team/', views.team, name = "team"),
    path('home2/', views.home2, name = "home2"),
    path('advisory/', views.advisory, name = "advisory"),
    path('secretariat/', views.secretariat, name = "secretariat"),
    path('achievements/', views.achievements, name = "achievements"),
   
]
