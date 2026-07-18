from django.urls import path
from contact.views import MyProfileAPI, ContactAPI, ContactIndividualAPI

urlpatterns = [
    path('myprofile/', MyProfileAPI.as_view(), name='my_profile'),
    path('', ContactAPI.as_view(), name='contact'),
    path('<str:n>/', ContactIndividualAPI.as_view(), name='contact_individual'),
]
