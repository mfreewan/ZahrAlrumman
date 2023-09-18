from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
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

class InKindDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InKindDonation
        fields = ('id','Name','Email','PhoneNumber','Country','TypeOfDonation','AmountOfDonation')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields =("username","id",) 

class CashDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashDonation
        fields = ('__all__')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('__all__')

class ExistingProjectsSerializer(serializers.ModelSerializer):
    class Meta :
        model = ExistingProjects
        fields = ('__all__')

class AboutSerializer(serializers.ModelSerializer):
    class Meta :
        model = About
        fields = ('__all__')

class NumberOfAchievementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NumberOfAchievements
        fields = ('__all__')

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ('__all__')



