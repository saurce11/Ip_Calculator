from django.urls import path
from . import views

urlpatterns = [
    path('', views.ip_info, name='ip_info'),  # Маршрут для страницы с формой
]
