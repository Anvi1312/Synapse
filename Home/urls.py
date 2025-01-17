from django.urls import path
from Home import views
from .views import index, hospital_login, logout_view, bed_management
# prototype/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Role and Login Paths
    path('map/', views.map, name='map'),
    path('lab/', views.lab, name='lab'),
    path('trends/', views.trends, name='health'),
    path('insurance/', views.insurance, name='insurance'),
    path('trends/', views.trends, name='trends'),
    path('patient_lab/', views.patient_lab, name='patient_lab'),
    path('in_patient/', views.in_patient, name='in_patient'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('queue-management/', views.queue_management, name='queue_management'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('ot/', views.ot, name='ot'),
    path('order/', views.order, name='order'),
    path('pharmacy/', views.pharmacy, name='pharmancy'),
    path('bill/', views.bill, name='bill'),
    path('interhospital/', views.interhospital, name='interhospital'),
    path('lab/', views.lab, name='lab'),
    path('medical_records/', views.medical_records, name='medical_records'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('appointment_booking/', views.appointment_booking, name='patient_dashboard'),
    path('radiology/', views.radiology, name='radiology'),
    path('out_patient/', views.out_patient, name='out_patient'),
    path('clinical/', views.clinical, name='clinical'),
    path('admin/', admin.site.urls),
    path('', views.role_selection, name="role_selection"),
    path('logout/', views.logout_view, name="logout"),
    path('hospital-login/', views.hospital_login, name='hospital_login'),
    path('patient-login/', views.patient_login, name="patient_login"),
    path('role-selection/', views.role_selection, name="role_selection"),

    # Patient Registration and Details
    path('patient-registration/', views.patient_registration, name='patient_registration'),
    path('patient-details/<str:aadhaar_number>/', views.patient_detail, name="patient_details"),
    path('patient-list/', views.patient_list, name='patient_list'),

    # Dashboard and Medical Records
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('medical-records/', views.medical_records, name='medical_records'),
    path('appointments/', views.appointment_schedule, name='appointment_schedule'),

    # Hospital and Bed Management
    path('bed-management/', views.bed_management, name='bed_management'),
    
    # Appointment Management Views
    path('appointment-management/', views.appointment_management, name='appointment_management'),
    path('appointment-detail/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment-update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment-delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),

    # In-Patient, Out-Patient, and Clinical Views

    # Index Path
    path('index/', views.index, name='index'),
]