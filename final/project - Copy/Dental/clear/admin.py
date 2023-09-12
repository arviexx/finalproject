from django.contrib import admin
from .models import ContactMessage
from .models import Appointment

admin.site.register(Appointment)
admin.site.register(ContactMessage)