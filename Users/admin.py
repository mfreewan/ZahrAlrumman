from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm ,CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'username',
        'email',
        'is_staff',
    )
    fieldsets = UserAdmin.fieldsets +( (None , {"fields":(
            "MiddleName",
            "NationalNumber",
            "RegisterDate",
            "FamilyNumbers",
            "NAF",)}), )
    add_fieldsets = UserAdmin.add_fieldsets + ( (None , {"fields":(
            "first_name",
            "MiddleName",
            "last_name",
            "NationalNumber",
            "RegisterDate",
            "FamilyNumbers",
            "NAF",)}), )

admin.site.register(CustomUser,CustomUserAdmin)