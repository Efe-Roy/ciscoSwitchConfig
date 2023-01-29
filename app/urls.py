from django.urls import path
from .views import configure_switch

urlpatterns = [
    path('configure/', configure_switch, name='configure_switch'),
]
