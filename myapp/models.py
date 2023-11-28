from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.generic.models import IBANField, PhoneNumberField

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, null=True)
    iban = IBANField(blank=True, null=True)

