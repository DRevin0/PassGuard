from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('check-leak/', views.check_leak, name = 'check_leak'),
    path('check-strength/', views.check_strength, name='check_strength'),
    path('generate-password/', views.generate_password_view, name='generate_password'),
]
