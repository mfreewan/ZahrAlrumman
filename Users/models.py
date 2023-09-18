from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



# Create your models here.

class CustomUser(AbstractUser):
    number_validator = RegexValidator(
        regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
        message="number must contain 10 digits",
    )
    first_name = models.CharField(
        help_text="enter your first name", max_length=30, blank=True
    )
    MiddleName = models.CharField(
        max_length=200, help_text="Enter a user middle name", null=True, blank=True
    )
    last_name = models.CharField(
        help_text="enter your last name", max_length=30, blank=True   
        )
    NationalNumber = models.CharField(
        validators=[number_validator],
        max_length=10,
        help_text="Enter a user National Number",
        null=False,
        blank=False,
    )
    RegisterDate = models.DateField(null=True, blank=True)
    FamilyNumbers = models.IntegerField(
        help_text="number of family numbers ", default=0
    )
    NAF = models.BooleanField(default=False)
