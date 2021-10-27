from django.urls import path
from .import views
urlpatterns = [
     path('', views.event, name = "event"),
     path('<int:event_id>', views.singleevent, name = "singleevent"),
]
