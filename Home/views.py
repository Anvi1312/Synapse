from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PatientRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render
from .models import Appointment  # Import your Appointment model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Appointment
from .forms import AppointmentForm  # Make sure you have a form for handling appointment data

# views.py
from django.shortcuts import render

def insurance(request):
    return render(request, 'insurance.html')

def trends(request):
    return render(request, 'trends.html')

def map(request):
    return render(request, 'map.html')

def patient_lab(request):
    return render(request, 'patient_lab.html')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def appointment_booking(request):
    return render(request, 'appointment_booking.html')

def medical_record(request):
    return render(request, 'medical_records.html')

def radiology(request):
    return render(request, 'radiology.html')


def lab(request):
    return render(request, 'lab.html')


def pharmacy(request):
    return render(request, 'pharmacy.html')

def interhospital(request):
    return render(request, 'interhospital.html')

def bill(request):
    return render(request, 'bill.html')

def order(request):
    return render(request, 'order.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def ot(request):
    return render(request, 'ot.html')

def queue_management(request):
    return render(request, 'queue_management.html')

def clinical(request):
    return render(request, 'clinical.html')


def in_patient(request):
    return render(request, 'in_patient.html')

class AppointmentView(View):
    def get(self, request):
        # Handle GET requests
        appointments = Appointment.objects.all()  # Fetch all appointments
        return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

    def post(self, request):
        # Handle POST requests (e.g., form submission)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save new appointment
            return redirect('appointment_list')  # Redirect to appointment list or another view
        return render(request, 'appointments/appointment_form.html', {'form': form})

class AppointmentDetailView(View):
    def get(self, request, pk):
        # Handle GET request for a single appointment detail
        appointment = get_object_or_404(Appointment, pk=pk)
        return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

class AppointmentUpdateView(View):
    def get(self, request, pk):
        # Handle GET request to edit an appointment
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentForm(instance=appointment)
        return render(request, 'appointments/appointment_form.html', {'form': form})

    def post(self, request, pk):
        # Handle POST request to update an appointment
        appointment = get_object_or_404(Appointment, pk=pk)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()  # Save the updated appointment
            return redirect('appointment_detail', pk=pk)  # Redirect to the appointment detail view
        return render(request, 'appointments/appointment_form.html', {'form': form})

class AppointmentDeleteView(View):
    def get(self, request, pk):
        # Handle GET request to confirm deletion
        appointment = get_object_or_404(Appointment, pk=pk)
        return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})

    def post(self, request, pk):
        # Handle POST request to delete an appointment
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return redirect('appointment_list')  # Redirect to the list view after deletion

def appointment_management(request):
    # Get all appointments
    appointments = Appointment.objects.all()
    
    # Pass appointments to template
    context = {
        'appointments': appointments,
    }
    
    return render(request, 'appointment_management.html', context)


def bed_management(request):
    return render(request, 'bed_management.html')

@login_required
def index(request):
    # Handle the index page logic
    return render(request, 'index.html')

@login_required
def hospital_login(request):
    # Handle the login logic
    return render(request, 'hospital_login.html')

@login_required
def logout_view(request):
    # Handle logout logic
    # You might want to use Django's built-in logout view
    from django.contrib.auth import logout
    logout(request)
    return redirect('hospital_login')

@login_required
def role_selection(request):
    # Handle role selection logic
    return render(request, 'role_selection.html')

@login_required
def bed_management(request):
    # Handle bed management logic
    # You can add context data here if needed
    return render(request, 'bed_management.html')

@login_required
def in_patient(request):
    # You can add any context here if needed, for example, patient data or bed status
    return render(request, 'in_patient.html')

# Out-Patient Page View
@login_required
def out_patient(request):
    # You can add any context here if needed, for example, patient data or treatment stats
    return render(request, 'out_patient.html')

# Clinical Page View
@login_required
def clinical(request):
    # You can add any context here if needed, for example, clinical statistics or doctor data
    return render(request, 'clinical.html')

# Role selection page
def role_selection(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'hospital':
            return redirect('hospital_login')
        elif role == 'patient':
            return redirect('patient_login')
    return render(request, 'role_selection.html')

# Hospital login view
def hospital_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the main page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'hospital_login.html')

# Patient login view
def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')  # Redirect to the main page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'patient_login.html')

# Index page
def index(request):
    if request.user.is_anonymous:
        return redirect('role_selection')  # Redirect to role selection if user is not logged in
    return render(request, 'index.html')

# Hospital login view
def hospital_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a success page or dashboard
        else:
            # Handle login error (e.g., invalid credentials)
            pass
    return render(request, 'hospital_login.html')
def logoutuser(request):
    logout(request)
    messages.warning(request, "Logged Out Successfully!")
    return redirect('role_selection')  # Redirect to role selection after logout

# Patient registration view
def patient_registration(request):
    if request.method == 'POST':
        patient = PatientRegistrationForm(
            title=request.POST.get('title'),
            first_name=request.POST.get('first-name'),
            middle_name=request.POST.get('middle-name'),
            last_name=request.POST.get('last-name'),
            birth_first_name=request.POST.get('birth-first-name'),
            birth_middle_name=request.POST.get('birth-middle-name'),
            birth_last_name=request.POST.get('birth-last-name'),
            dob=request.POST.get('dob'),
            gender_identity=request.POST.get('gender-identity'),
            sex=request.POST.get('sex'),
            sexual_orientation=request.POST.get('sexual-orientation'),
            marital_status=request.POST.get('marital-status'),
            address=request.POST.get('address'),
            address_line2=request.POST.get('address-line2'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            postal_code=request.POST.get('postal-code'),
            country=request.POST.get('country'),
            mobile_number=request.POST.get('mobile-number'),
            emergency_contact=request.POST.get('emergency-contact'),
            mother_name=request.POST.get('mother-name'),
            father_name=request.POST.get('father-name'),
            email=request.POST.get('email'),
            aadhaar_number=request.POST.get('aadhaar-number'),
        )
        patient.save()
        messages.success(request, 'Patient registered successfully!')
        return redirect('patient_registration')  # Redirect back to registration page
    return render(request, 'patient_registration.html')

def patient_list(request):
    patients = PatientRegistrationForm.objects.all()
    return render(request, 'view_patient_list.html', {'patients': patients})

def patient_detail(request, aadhaar_number):
    patient = get_object_or_404(PatientRegistrationForm, aadhaar_number=aadhaar_number)
    return render(request, 'view_details_patients.html', {'patient': patient})

# Patient Dashboard View
@login_required
def patient_dashboard(request):
    # You can pass additional context such as patient details here
    return render(request, 'patient_dashboard.html')

# Medical Records View
@login_required
def medical_records(request):
    # Logic for retrieving medical records from the database
    # Add context for records if needed
    return render(request, 'medical_records.html')

# Appointment Schedule View
@login_required
def appointment_schedule(request):
    # Logic for retrieving and managing appointments
    return render(request, 'appointment_schedule.html')