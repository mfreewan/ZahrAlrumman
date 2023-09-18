from django import forms
from Users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import InKindDonation, CashDonation, Idea, Volunteer


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phoneNumber = forms.CharField(required=True)
    mailing_address = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phoneNumber",
            "mailing_address",
            "NationalNumber",
            "FamilyNumbers",
            "NAF",
        )


class InKindDonationForm(forms.ModelForm):
    class Meta:
        model = InKindDonation
        fields = (
            "Name",
            "Email",
            "PhoneNumber",
            "Country",
            "TypeOfDonation",
            "AmountOfDonation",
        )


class CashDonationForm(forms.ModelForm):
    class Meta:
        model = CashDonation
        fields = ("Name", "Email", "PhoneNumber", "Country", "Cash")


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = (
            "idea",
            "name",
            "PhoneNumber",
        )


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ["username", "RegisterDate", "RegisterDate"]