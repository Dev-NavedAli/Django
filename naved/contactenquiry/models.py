from django.db import models

class contactEnquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    website_name = models.CharField(max_length=50)
    manage  = models.CharField(max_length=50)