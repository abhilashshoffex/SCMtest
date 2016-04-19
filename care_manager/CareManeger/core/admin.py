from django.contrib import admin

# Register your models here.
from .models import Registration

class RegistrationAdmiin(admin.ModelAdmin):
	list_display = ['full_name', 'contact']

admin.site.register(Registration, RegistrationAdmiin)