from django.contrib import admin
from contactenquiry.models import contactEnquiry

class contactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website_name', 'manage') 

admin.site.register(contactEnquiry,contactEnquiryAdmin)
