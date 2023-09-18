from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from main.models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    NumberOfAchievements,
    ExistingProjects,
    About,
    Idea,
    
)

from django.shortcuts import render
from rest_framework import generics , permissions , viewsets
from .serializers import (
InKindDonationSerializer, 
UserSerializer,
CashDonationSerializer,
NewsSerializer,
EventsSerializer,
ExistingProjectsSerializer ,
AboutSerializer , 
NumberOfAchievementsSerializer,
IdeaSerializer,
) 
from django.contrib.auth import get_user_model
from .permissions import IsUserOrReadOnly , IsSuperAdmin
from rest_framework.permissions import IsAdminUser

class InKindDonationViewSet(viewsets.ModelViewSet):

    queryset = InKindDonation.objects.all()
    serializer_class = InKindDonationSerializer

    def get_permissions(self):
        # for i in self.action :
        #     print(i)
        # print(self.action)
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperAdmin]

        return [permission() for permission in permission_classes]

class CashDonationsViewSet(viewsets.ModelViewSet) :
    
    queryset = CashDonation.objects.all()
    serializer_class = CashDonationSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperAdmin]

        return [permission() for permission in permission_classes]



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer  

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer 

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]  

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes] 
    
class ExistingProjectsViewSets(viewsets.ModelViewSet):
    queryset = ExistingProjects.objects.all()
    serializer_class = ExistingProjectsSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes] 

class AboutViewSets(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes] 

class NumberOfAchievementsViewSets(viewsets.ModelViewSet):
    queryset = NumberOfAchievements.objects.all()
    serializer_class = NumberOfAchievementsSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes] 

from .models import Idea

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()    
    serializer_class = IdeaSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperAdmin]

        return [permission() for permission in permission_classes]        
