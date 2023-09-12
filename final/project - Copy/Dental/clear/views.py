from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Appointment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import AppointmentApprovalForm, AppointmentForm, RegisterUserForm
from .forms import ContactForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect


def index(request):
    return render(request, 'users/index.html') 
def team(request):
    return render(request, 'users/team.html')       
def loginuser(request):
    return render(request, 'users/loginuser.html')
def loginadmin(request):
    return render(request, 'users/loginadmin.html')
def adminpage(request):
    return render(request, 'users/adminpage.html')
def userpage(request):
    return render(request, 'users/userpage.html')
def services(request):
    return render(request, 'users/services.html')
def doctors(request):
    return render(request,'users/doctors.html')


def aboutus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('userpage')  
    else:
        form = ContactForm()

    return render(request, 'users/aboutus.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)

        
        return redirect('loginuser')  
    else:
        return render(request, 'users/register_user.html')



def check_username(request):
    username = request.GET.get('username', None)
    data = {'exists': User.objects.filter(username=username).exists()}
    return JsonResponse(data)

def check_email(request):
    email = request.GET.get('email', None)
    data = {'exists': User.objects.filter(email=email).exists()}
    return JsonResponse(data)

def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return HttpResponseRedirect(reverse('userpage'))
        else:

            messages.error(request, 'Invalid username or password. Please check and try again.')
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'users/loginuser.html', {'form': form})



def loginadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('adminpage')
        else:
            
            return render(request, 'users/loginadmin.html', {'error_message': 'This is for Admin Staff Only!'})
    else:
        return render(request, 'users/loginadmin.html')




def appointmentforms(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')  
    else:
        form = AppointmentForm()
    
    return render(request,'users/appointmentforms.html', {'form': form})

def appointments(request):
    appointments = Appointment.objects.all().order_by('-id')
    return render(request,'users/records.html', {'appointments':appointments})




def delete_appointment(request, appointment_id):
    try:
        appointment_instance = get_object_or_404(Appointment, pk=appointment_id)
        appointment_instance.delete()
       
        return redirect('records')  
    except Appointment.DoesNotExist:
        return HttpResponse("Appointment does not exist.")


def adminrecords(request):
    appointments = Appointment.objects.all().order_by('-id')
    return render(request,'users/adrecords.html', {'appointments':appointments})


def approve_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        approval_form = AppointmentApprovalForm(request.POST, instance=appointment)
        if approval_form.is_valid():
             
                appointment.approval = True
                appointment.approval_message = "Appointment confirmed.Thank you!"
           
             
                   
                appointment.save()
                return redirect('adminrecords') 

    else:
        approval_form = AppointmentApprovalForm(instance=appointment)

    return render(request, 'adminpage.html', {'approval_form': approval_form})

def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        approval_form = AppointmentApprovalForm(request.POST, instance=appointment)
        if approval_form.is_valid():
             
                appointment.approval = True
                appointment.approval_message = "Your request is declined."
             
                   
                appointment.save()
                return redirect('adminrecords') 

    else: 
        approval_form = AppointmentApprovalForm(instance=appointment)

    return render(request, 'adminpage.html', {'approval_form': approval_form})














    
    
    
    
    


