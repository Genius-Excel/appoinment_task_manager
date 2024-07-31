from django.urls import path
from . import views

urlpatterns = [
    path('api/create-appointment/', views.CreateClientAppointment.as_view()),

]