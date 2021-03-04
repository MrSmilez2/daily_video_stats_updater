from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Influencer, Content, DailyStats
from youtube_database.youtube_api_logic.login_to_api import get_video_stats
from youtube_database.database_update_logic.daily_content_update import create_daily_video_stat
# from datetime import date
#
# import os
# import pickle
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# Create your views here.

class InfluencerView(ListView):
    model = Influencer
    paginate_by = 1


class ContentView(ListView):
    model = DailyStats
    paginate_by = 10
    ordering = ['-video_url__date_of_publication']
    create_daily_video_stat()
    # all_videos = Content.objects.all()
    # list_of_urls = [el.video_url for el in all_videos]
    # print(list_of_urls)
    # daily_results = get_video_stats(list_of_urls)
    # for video in daily_results:
    #     video_object = None
    #     if DailyStats.objects.filter(video_url__video_url=video['video_id']).exists():
    #         video_object = DailyStats.objects.filter(video_url__video_url=video['video_id']).latest('date_of_update')
    #     current_video = Content.objects.get(video_url=video['video_id'])
    #     if video_object is None:
    #         todays_video = DailyStats.objects.create(
    #             video_url=current_video,
    #             date_of_update=video['today'],
    #             video_views=video['video_views'],
    #             video_comments=video['video_comments'],
    #             video_likes=video['video_likes'],
    #             video_dislikes=video['video_dislikes']
    #         )
    #     else:
    #         if video_object.date_of_update != video['today'].date():
    #             todays_video = DailyStats.objects.create(
    #                 video_url=current_video,
    #                 date_of_update=video['today'],
    #                 video_views=video['video_views'],
    #                 video_comments=video['video_comments'],
    #                 video_likes=video['video_likes'],
    #                 video_dislikes=video['video_dislikes']
    #             )
        # q = Q(video_url=video['video_id']) & Q(date_of_update=video['today'])
        # test = DailyStats.objects.get_or_create(q)

    # print(daily_results)




