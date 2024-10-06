from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
import re
from .models import Appointment, ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class AppointmentApprovalForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['approval_message']
        approval_message = forms.CharField(widget=forms.Textarea, required=False)
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'gender',
            'phone_number',
            'email',
            'address',
            'appointment_date',
            'appointment_time',
            'doctor',
            'Teeth_Extractions',
            'Dental_Cleaning',
            'Dental_Crowns',
            'Teeth_Whitening',
            'Cosmetics_Dentistry'

        ]

        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date','class': 'datepicker'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time','class': 'timepicker'}),
            
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if phone_number:
                if not re.match(r'^(\+639|\b09)\d{9}$', phone_number):
                    raise forms.ValidationError('Please enter a valid Philippine Number.')
            return phone_number
        
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date:
     
            if appointment_date.weekday() not in [0, 1, 2, 3, 4]:
                raise forms.ValidationError('Appointment date must be a weekday (Monday to Friday)')


            today = datetime.date.today()
            if appointment_date <= today:
                raise forms.ValidationError('Appointment date must be in the future')

         
            holidays = [
                  datetime.date(2024,1,1),
                    datetime.date(2024,1,16),
                    datetime.date(2024,2,20),
                    datetime.date(2024,4,10),
                    datetime.date(2024,5,29),
                    datetime.date(2024,7,4),                 
                    datetime.date(2024,9,4),
                    datetime.date(2024,10,9),
                    datetime.date(2024,11,11),
                    datetime.date(2024,11,23),
                    datetime.date(2024,12,25),
                    datetime.date(2024,3,17),
                    datetime.date(2024,5,5),
                    datetime.date(2024,6,19),
                    datetime.date(2024,10,31),
                    datetime.date(2024,12,31),
               
            ]
            if appointment_date in holidays:
                raise forms.ValidationError('Appointment date cannot be a holiday.')

            return appointment_date

    def clean_appointment_time(self):
        appointment_time = self.cleaned_data.get('appointment_time')
        if appointment_time:
            start_time = datetime.time(8, 0)
            end_time = datetime.time(17, 0)

            if not (start_time <= appointment_time <= end_time):
                raise forms.ValidationError('Appointment time must be between 8 am and 5 pm.')

            return appointment_time