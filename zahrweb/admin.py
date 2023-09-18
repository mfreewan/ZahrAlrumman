from django.contrib import admin

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from django.contrib import admin
from main.models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    Achievements,
    ExistingProjects,
    About,
    Nav,
    EventRegister,
)


# # Define a custom admin page for the User model
# class CustomUserAdmin(UserAdmin):
#     # Specify the model the custom admin page should use
#     model = User
#     # Specify which fields to display in the list view
#     list_display = [
#         "username",
#         "email",
#         "first_name",
#         "last_name",
#         "is_staff",
#         "is_active",
#         "is_volunteer",
#         "phoneNumber",
#     ]

#     # Specify which filters should be available on the right side of the list view
#     list_filter = ["is_staff", "is_active", "is_volunteer"]
#     # Define the sections and fields to be displayed on the edit page for an individual user
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (
#             "Personal info",
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                     "email",
#                     "NationalNumber",
#                     "phoneNumber",
#                     "MiddleName",
#                     "RegisterDate",
#                     "FamilyNumbers",
#                     "NAF",
#                 )
#             },
#         ),
#         ("Permissions", {"fields": ("is_active", "is_staff", "is_volunteer")}),
#         # ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     # Define the sections and fields to be displayed on the add page when creating a new user
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "username",
#                     "email",
#                     "first_name",
#                     "last_name",
#                     "password1",
#                     "password2",
#                     "NationalNumber",
#                     "phoneNumber",
#                     "MiddleName",
#                     "RegisterDate",
#                     "FamilyNumbers",
#                     "NAF",
#                 ),
#             },
#         ),
    # )
    # # Specify which fields should be searchable in the search bar
    # search_fields = ("username", "email", "first_name", "last_name")
    # # Specify the default ordering of the list view
    # ordering = ("username",)


class NewsAdmin(admin.ModelAdmin):
    list_display = ("Title", "Image", "Details")
    list_filter = ["date"]


class ExistingProjectsAdmin(admin.ModelAdmin):
    list_display = ("Name", "Details", "start_date")
    list_filter = ["start_date"]
    fields = ("Name", "start_date", "Details", "Image")


class VolunteersAdmin(admin.ModelAdmin):
    list_display = ("field_of_volunteers", "RegisterDate")
    fields = ("field_of_volunteers", "RegisterDate")


# Define a new class called 'class name'Admin which inherits from admin.ModelAdmin
# Since there is no code inside the class, simply use pass to avoid syntax errors
class InKindDonationAdmin(admin.ModelAdmin):
    pass


class CashDonationAdmin(admin.ModelAdmin):
    pass


class EventsAdmin(admin.ModelAdmin):
    pass


class posterAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


class NumberOfAchievementsAdmin(admin.ModelAdmin):
    pass


class numberadmin(admin.ModelAdmin):
    pass


class EventRegisteradmin(admin.ModelAdmin):
    pass


from django.urls import reverse
from django.utils.html import format_html


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("username", "user_profile_link")

    def user_profile_link(self, obj):
        if obj.username:
            url = reverse("user_profile", args=[str(obj.username.id)])
            return format_html('<a href="{}">{}</a>', url, obj.username.username)
        else:
            return "error"


class NavAdmin(admin.ModelAdmin):
    pass


# Register the Classes Admin object with the admin site so that it can be used to modify our classes objects
admin.site.register(ExistingProjects, ExistingProjectsAdmin)
admin.site.register(InKindDonation, InKindDonationAdmin)
admin.site.register(CashDonation, CashDonationAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(poster, posterAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Achievements, NumberOfAchievementsAdmin)
# admin.site.register(number, numberadmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Nav, NavAdmin)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(EventRegister, EventRegisteradmin)
