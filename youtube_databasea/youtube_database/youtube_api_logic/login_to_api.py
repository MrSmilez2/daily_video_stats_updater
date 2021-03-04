import os
import pickle
from youtube_database.models import Content
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date, datetime


def get_video_stats(list_of_urls):
    credentials = None


    # token.pickle stores the user's credentials from previously successful logins
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'youtube_database/youtube_api_logic/client_secrets.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.readonly'
                ]
            )

            flow.run_local_server(port=8080, prompt='consent',
                                  authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    youtube = build('youtube', 'v3', credentials=credentials)


    request = youtube.videos().list(
        part=['snippet', 'statistics', 'id'],
        id=list_of_urls,
    )
    response = request.execute()
    test = Content.objects.all()
    result_list = []
    print(123123123, test)
    for el in response['items']:
        today = datetime.strptime(f"{date.today()}", "%Y-%m-%d")
        result_dict = {'video_id': el['id'], 'date_created': el['snippet']['publishedAt'],
                       'channel_url': el['snippet']['channelId'], 'video_name': el['snippet']['title'],
                       'video_views': el['statistics']['viewCount'], 'video_likes': el['statistics']['likeCount'],
                       'video_comments': el['statistics']['commentCount'],
                       'video_dislikes': el['statistics']['dislikeCount'],
                       'today': today}
        result_list.append(result_dict)

    return result_list
# print(response['items'][0]['statistics'])

def get_credentials():
    credentials = None

    # token.pickle stores the user's credentials from previously successful logins
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no valid credentials available, then either refresh the token or log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                'youtube_database/youtube_api_logic/client_secrets.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.readonly'
                ]
            )

            flow.run_local_server(port=8080, prompt='consent',
                                  authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)
    return credentials

def get_youtube_video_stats(credentials, list_of_urls):
    '''here I create a list of dicts which contains all video statistics'''
    youtube = build('youtube', 'v3', credentials=credentials)

    request = youtube.videos().list(
        part=['snippet', 'statistics', 'id'],
        id=list_of_urls,
    )
    response = request.execute()
    test = Content.objects.all()
    result_list = []
    print(123123123, test)
    for el in response['items']:
        today = datetime.strptime(f"{date.today()}", "%Y-%m-%d")
        result_dict = {'video_id': el['id'], 'date_created': el['snippet']['publishedAt'],
                       'channel_url': el['snippet']['channelId'], 'video_name': el['snippet']['title'],
                       'video_views': el['statistics']['viewCount'], 'video_likes': el['statistics']['likeCount'],
                       'video_comments': el['statistics']['commentCount'],
                       'video_dislikes': el['statistics']['dislikeCount'],
                       'today': today}
        result_list.append(result_dict)
    return result_list