from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadHome),
    path('process_money', views.findGold),
    path('total_reset', views.resetGold),
]

