from django.urls import path
from .views import profGetAdd
urlpatterns = [
    path('prof/', profGetAdd)
]