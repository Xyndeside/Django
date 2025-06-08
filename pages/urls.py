from django.urls import path

from .views import HomePageView, ResumePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', ResumePageView.as_view(), name='resume'),
]