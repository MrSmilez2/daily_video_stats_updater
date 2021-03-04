from django.urls import path
from youtube_database.views import InfluencerView, ContentView


urlpatterns = [
    path('', InfluencerView.as_view(), name='influencers'),
    path('content', ContentView.as_view(), name='content'),
]