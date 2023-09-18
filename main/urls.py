from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import  UserViewSet ,InKindDonationViewSet,CashDonationsViewSet,NewsViewSet,EventsViewSet ,ExistingProjectsViewSets ,AboutViewSets ,NumberOfAchievementsViewSets , IdeaViewSet 
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register("users",UserViewSet,basename="users")
router.register("inkinddonation",InKindDonationViewSet,basename="in_kind_donation")
router.register("cashdonation",CashDonationsViewSet,basename='cash_donation')
router.register("news",NewsViewSet,basename='news')
router.register("events",EventsViewSet,basename='events')
router.register("ExistingProjects",ExistingProjectsViewSets,basename='ExistingProjects')
router.register("about",AboutViewSets,basename='about')
router.register("achievements",NumberOfAchievementsViewSets,basename='achievements')
router.register("idea",IdeaViewSet,basename='idea')
# router.register('index',views.index,basename='index')


urlpatterns = router.urls


