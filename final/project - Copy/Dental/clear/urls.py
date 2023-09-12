from django.urls import path
from . import views





urlpatterns = [
    path('', views.index, name='index'),
    path('appointments/',views.appointments, name='records'),
    path('adminrecords/',views.adminrecords, name='adminrecords'),
    path('appointmentforms/',views.appointmentforms, name='appointmentforms'),
    path('register_user', views.register_user, name='register_user'),
    path('team/', views.team, name='team'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('loginadmin/', views.loginadmin, name='loginadmin'),
    path('userpage/', views.userpage, name='userpage'),
    path('services/', views.services, name='services'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('doctors/', views.doctors, name='doctors'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
   path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
   path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
 
    ]


