from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='say-hello'),
    path('api/create-appointment/', views.CreateClientAppointment.as_view()),

]