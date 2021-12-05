from django.urls import path
from .import views
#from django.urls import reverse_lazy

urlpatterns = [
     path('login', views.login, name = "login"),
     path('register', views.register, name = "register"),
     path('logout', views.logout, name = "logout"),
     path('dashboard', views.dashboard, name = "dashboard"),
     path('downloadpdfform', views.downloadpdfform, name = "downloadpdfform"),
     path('pdfgenerator', views.pdfgenerator, name = "pdfgenerator"),
     path('reset', views.reset, name = "reset"),
     #change password
     #path('reset', auth_views.PasswordChangeView.as_view(), name='reset'),
     #path('reset_password/',auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')), name="reset_password"),
     #path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     #path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
