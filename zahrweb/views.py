from django.shortcuts import render
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
)
from audioop import reverse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import (
    InKindDonationForm,
    CashDonationForm,
    IdeaForm,
    VolunteerForm,
    EventRigesterForm,
    SignupForm,
)


# Create your views here.
# Define a view to retrieve data from different models and pass them as context to the "index.html" template
def index(request):
    # Retrieve the 5 latest poster objects from the database, ordered by their primary key in descending order (most recent first)
    posters = poster.objects.all().order_by("-id")[:5]
    # Retrieve the 3 most recent News objects from the database, ordered by their date in descending order (most recent first)
    news = News.objects.order_by("-date")[:3]
    # Retrieve all the number objects from the database
    number_of_achievements = Achievements.objects.all()
    # Retrieve the 3 most recently started ExistingProjects objects from the database, ordered by their start_date in descending order (most recent first)
    active_projects = ExistingProjects.objects.order_by("-start_date")[:3]
    # Retrieve all Event objects from the database
    events = Events.objects.all()
    # Retrieve all Nav objects from the database
    nav = Nav.objects.all()

    # Create a dictionary context with all the retrieved objects or lists as the values for their respective keys
    context = {
        "poster_image": posters,
        "news": news,
        "number_of_achievements": number_of_achievements,
        "active_projects": active_projects,
        "events": events,
        "nav": nav,
    }

    # Return the context dictionary and render the "index.html" template
    return render(request, "home/index.html", context=context)


# Define a view to retrieve a single News object from the database and pass it as context to the "news_detail.html" template
def detail(request, primary_key):
    # Retrieve a single News object from the database based on the primary key passed into the view
    news = News.objects.get(pk=primary_key)
    # Create a dictionary context with the retrieved News object as the value for the key "news"
    context = {"news": news}
    # Return the context dictionary and render the "news_detail.html" template
    return render(request, "details/news_detail.html", context)


# Define a view to retrieve a single Events object from the database and pass it as context to the "event_detail.html" template
def event_detail(request, primary_key):
    # Retrieve a single Events object from the database based on the primary key passed into the view
    events = Events.objects.get(pk=primary_key)
    # Create a dictionary context with the retrieved Events object as the value for the key "event"
    context = {"event": events}
    # Return the context dictionary and render the "event_detail.html" template
    return render(request, "details/event_detail.html", context)


# Define a view to retrieve a single ExistingProjects object from the database and pass it as context to the "project_detail.html" template
def project_detail(request, primary_key):
    # Retrieve a single ExistingProjects object from the database based on the primary key passed into the view
    project = ExistingProjects.objects.get(pk=primary_key)
    # Create a dictionary context with the retrieved ExistingProjects object as the value for the key "projects"
    context = {"projects": project}
    # Return the context dictionary and render the "project_detail.html" template
    return render(request, "details/project_detail.html", context)


# Define a view to retrieve all About objects from the database and pass them as context to the "about.html" template
def about(request):
    # Retrieve all About objects from the database
    abouts = About.objects.all()
    # Create a dictionary context with the retrieved About objects as the value for the key "abouts"
    context = {"abouts": abouts}
    # Return the context dictionary
    return context


# Define a view to create a table containing project data and pass it as context to the "about.html" template
def my_table(request):
    # Define a list of dictionaries, each describing a project and its attributes
    data = [
        {
            "project": "مشروع مكاني",
            "supporter": "UNICEF",
            "audience": "-الاطفال السوريين و الاردنيين من عمر ( 0-18 ) - اليافعين ( 18-24 ) - الامهات السوريات و الاردنيات",
            "cost": "110,000 دينار سنويا",
        },
        {
            "project": "مشروع التوعية ( ACF )",
            "supporter": "ACF",
            "audience": "السوريين و الاردنيين من عمر ( 18-45 )",
            "cost": "20,000 دينار سنويا",
        },
        {
            "project": "مشروع ترخيص المشاريع المنزلية الصغيرة ( IRD )",
            "supporter": "UNHCR",
            "audience": "اصحاب المشاريع الصغيرة السوريين و الاردنيين",
            "cost": "38,000 دينار سنويا",
        },
        {
            "project": "مشروع مصنع المخللات",
            "supporter": "USAID",
            "audience": "المجتمع المحلي",
            "cost": "70,000 دينار",
        },
        {
            "project": "مشروع وزارة الشباب",
            "supporter": "البنك الدولي",
            "audience": "الشباب في مراكز الشباب في لوا بني كنانة",
            "cost": "48,000 دينار",
        },
    ]
    # Create a dictionary context with the project data as the value for the key "data"
    context = {"data": data}
    # Return the context dictionary
    return context


# Define a view to combine the data from the "about" and "my_table" views into a single context dictionary and render the "about.html" template
def my_view(request):
    # Call the "about" view to retrieve the About objects from the database
    abouts = about(request)
    # Call the "my_table" view to create a table of project data
    table = my_table(request)
    # Create an empty dictionary to hold the final context
    context = {}
    # Update the dictionary context with the "abouts" dictionary
    context.update(abouts)
    # Update the dictionary context with the "table" dictionary
    context.update(table)
    # Render the "about.html" template with the final context
    return render(request, "details/about.html", context)


# Define a function that handles requests to sign up a new user
def signup(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the SignupForm, passing in the POST data
        form = SignupForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():
            # If the form is valid, save it to the database and get the resulting user object
            user = form.save()
            # Redirect the user to another page (in this case, the homepage)
            return redirect("index")
    else:
        # If the request method is not POST, create a new instance of the SignupForm
        form = SignupForm()
    # Render the "signup.html" template, passing in the form as context
    # The context dictionary also includes any existing form input values, errors, etc.
    return render(request, "registration/signup.html", {"form": form})


# Define a function that handles requests to submit in-kind donations
def in_kind_donation(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the InKindDonationForm, passing in the POST data
        form = InKindDonationForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():
            # If the form is valid, save it to the database
            form.save()
            # Redirect the user to another page (in this case, the homepage)
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        # If the request method is not POST, create a new instance of the InKindDonationForm
        form = InKindDonationForm()
    # Render the "in_kind_donation.html" template, passing in the form as context
    return render(request, "forms/in_kind_donation.html", {"form": form})


# Define a function that handles requests to submit cash donations
def Cash_donation(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the CashDonationForm, passing in the POST data
        form = CashDonationForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():
            # If the form is valid, save it to the database
            form.save()
            # Redirect the user to another page (in this case, the homepage)
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        # If the request method is not POST, create a new instance of the CashDonationForm
        form = CashDonationForm()
    # Render the "cash_donation.html" template, passing in the form as context
    # The context dictionary also includes any existing form input values, errors, etc.
    return render(request, "forms/cash_donation.html", {"form": form})


# Define a function that handles requests to submit a new idea
def Idea(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the IdeaForm, passing in the POST data
        form = IdeaForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():
            # If the form is valid, save it to the database
            form.save()
            # Redirect the user to another page (in this case, the homepage)
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        # If the request method is not POST, create a new instance of the IdeaForm
        form = IdeaForm()
    # Render the "idea.html" template, passing in the form as context
    # The context dictionary also includes any existing form input values, errors, etc.
    return render(request, "forms/idea.html", {"form": form})


# Use the login_required decorator to ensure that only authenticated users can access this view
@login_required
# Define a function that handles requests to create a new volunteer
def volunteer_create(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the VolunteerForm, passing in the POST data
        form = VolunteerForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():  # If the form is valid, save it to the database
            volunteer = form.save(commit=False)
            # Set the volunteer's username as the currently logged in user
            volunteer.username = request.user
            # Save the volunteer to the database with the new username
            volunteer.save()
            # Redirect the user to another page (in this case, a success page)
            return redirect("index")
    else:
        # If the request method is not POST, create a new instance of the VolunteerForm
        form = VolunteerForm()
    # Render the "volunteer_form.html" template, passing in the form as context
    # The context dictionary also includes any existing form input values, errors, etc.
    return render(request, "forms/volunteer_form.html", {"form": form})


# Define a function that handles requests to register for an event
def event_register(request):
    # Check if the request method is POST (i.e. form has been submitted)
    if request.method == "POST":
        # Get an instance of the EventRigesterForm, passing in the POST data
        form = EventRigesterForm(request.POST)
        # Check if the submitted form is valid
        if form.is_valid():
            # If the form is valid, save it to the database
            form.save()
            # Redirect the user to another page (in this case, the homepage)
            return redirect("index")  # Replace `home` with your desired URL name
    else:
        # If the request method is not POST, create a new instance of the EventRigesterForm
        form = EventRigesterForm()
    # Render the "event_rigester.html" template, passing in the form as context
    return render(request, "forms/event_rigester.html", {"form": form})


from django.contrib.auth.models import User


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, "user_profile.html", {"user": user})
