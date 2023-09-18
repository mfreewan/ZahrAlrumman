from django.db import models
from django.core.validators import RegexValidator
from Users.models import CustomUser
from django.conf import settings

# Create your models here.
class CashDonation(models.Model):
    Name = models.CharField(max_length=100, help_text="Name of cash donation")
    Email = models.EmailField(
        max_length=100, help_text="Email address of cash donation"
    )
    PhoneNumber = models.IntegerField(help_text="Phone number of cash donation")
    Country = models.CharField(
        max_length=100, help_text="Country of cash donation member"
    )
    Cash = models.IntegerField(help_text="Cash donation")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


## Create a model for in_kind_donation information
class InKindDonation(models.Model):
    Name = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)   
    Email = models.EmailField(
        max_length=100, help_text="Email address of in kind donation"
    )
    PhoneNumber = models.IntegerField(help_text="Phone number of in kind donation")
    Country = models.CharField(max_length=100, help_text="Country of in kind donation")
    TypeOfDonation = models.CharField(max_length=100, help_text="Type of donation")
    AmountOfDonation = models.FloatField(max_length=200, help_text="Amount of donation")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


## Create a model for events
class Events(models.Model):
    NameOfEvent = models.CharField(max_length=100, help_text="Name of Event")
    Image = models.ImageField(
        upload_to="static/images",
        help_text="Image Poster for news ",
        default="default_image.jpg",
    )
    Location = models.CharField(max_length=100, help_text="Location of event")
    DateTimeOFEvent = models.DateTimeField(
        max_length=100, help_text="Date and time of event"
    )
    Description = models.TextField(max_length=400, help_text="Description of event")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.NameOfEvent


##Create a model for news
class News(models.Model):
    Title = models.CharField(max_length=100, help_text="Title of news")
    Image = models.ImageField(upload_to="static/images", help_text="Image Poster for news ")
    Details = models.TextField(max_length=30000, help_text="News details")
    date = models.DateField(help_text="Date of news")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Title


# create model that contain image poster for home page
class poster(models.Model):
    image = models.ImageField(upload_to="static/images",help_text="Image Poster for news ")
    details = models.CharField(max_length=100, help_text="News details")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.details


# create a model that contain number of achievements in the year
class Achievements(models.Model):
    Year = models.CharField(max_length=100,default=0, blank=True)
    FamilyAidNumber = models.IntegerField(default=0, help_text="Number of family aids ")
    ProjectsGrants = models.IntegerField(
        default=0, help_text="number of pojects grants"
    )
    EducationBeneficiaries = models.IntegerField(
        default=0, help_text="Number of education beneficiaries "
    )
    HomeProjects = models.IntegerField(default=0, help_text="Number of home projects ")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Year


# create a model that contain currently existing projects info
class ExistingProjects(models.Model):
    # Image = models.ImageField(max_length=400, help_text="project poster image ")
    Image = models.ImageField(upload_to="static/images",help_text="project poster image")

    Name = models.CharField(max_length=100, help_text="Name of project")
    Details = models.TextField(max_length=500, help_text="project details ")
    start_date = models.DateField(help_text="project start date")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


# Create a model that contains details and about of charitable assosiation info
class About(models.Model):
    About = models.TextField(
        max_length=100000, help_text="About charitable assosiation "
    )
    Image = models.ImageField(upload_to="static/images",help_text="insert about image ", default=0)

    def __str__(self):
        """string for represinting the model object"""

        return str(self.About)


#  Create a model that contains volunteering details
class Volunteer(models.Model):
    username = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Select a user name for the volunteer ",
    )
    volunteersCHOICES = (
        ("Computer", "Computer"),
        ("Projects", "Projects"),
        ("Education", "Education"),
    )
    field_of_volunteers = models.CharField(
        choices=volunteersCHOICES,max_length=100, help_text="type or field of voulnteer"
    )
    RegisterDate = models.DateField(help_text="Date of registration")


class Idea(models.Model):
    number_validator = RegexValidator(
        regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
        message="Phone number must contain 10 digits",
    )

    idea = models.TextField(help_text="enter your idea details : ")
    name = models.CharField(max_length=100, help_text="enter your name :")
    PhoneNumber = models.CharField(
        validators=[number_validator],
        max_length=10,
        blank=True,
        help_text="enter phone number",
    )  # validators should be a list

    def __str__(self):
        """string for represinting the model object"""

        return self.name


# this model contain fields for achivments years and numbers
class NumberOfAchievements(models.Model):
    year = models.IntegerField(default=0)
    home_project = models.IntegerField(default=0)
    project_grant = models.IntegerField(default=0)
    education_child = models.IntegerField(default=0)
    family_aid = models.IntegerField(default=0)

    def __str__(self):
        """string for represinting the model object"""

        return str(self.year)
    
# Create model to events user registrations


class EventRegister(models.Model):
    number_validator = RegexValidator(
        regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
        message="Phone number must contain 10 digits",
    )
    first_name = models.CharField(max_length=100, help_text="First Name ")
    last_name = models.CharField(max_length=100, help_text="First Name ")
    PhoneNumber = models.CharField(
        validators=[number_validator],
        max_length=10,
        blank=True,
        help_text="enter phone number",
    )

# this model to save nav bar image
class Nav(models.Model):
    Image = models.ImageField(upload_to="static/images", help_text="Image Poster for news ")
