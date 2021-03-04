from youtube_database.models import Content, DailyStats
from youtube_database.youtube_api_logic.login_to_api import get_credentials, get_youtube_video_stats

def create_daily_video_stat():
    credentials = get_credentials()
    all_videos = Content.objects.all()
    list_of_urls = [el.video_url for el in all_videos]
    print(list_of_urls)
    daily_results = get_youtube_video_stats(credentials, list_of_urls)
    for video in daily_results:
        video_object = None
        if DailyStats.objects.filter(video_url__video_url=video['video_id']).exists():
            video_object = DailyStats.objects.filter(video_url__video_url=video['video_id']).latest('date_of_update')
        current_video = Content.objects.get(video_url=video['video_id'])
        if video_object is None:
            todays_video = DailyStats.objects.create(
                video_url=current_video,
                date_of_update=video['today'],
                video_views=video['video_views'],
                video_comments=video['video_comments'],
                video_likes=video['video_likes'],
                video_dislikes=video['video_dislikes']
            )
        else:
            if video_object.date_of_update != video['today'].date():
                todays_video = DailyStats.objects.create(
                    video_url=current_video,
                    date_of_update=video['today'],
                    video_views=video['video_views'],
                    video_comments=video['video_comments'],
                    video_likes=video['video_likes'],
                    video_dislikes=video['video_dislikes']
                )