import json
import logging

import requests
from kafka import KafkaProducer
import sys
sys.path.append("/workspaces/YouTube-Metrics-Streamer/config")
from constants import YOUTUBE_API_KEY, PLAYLIST_ID

def youtube_video_statistics(video_id):
    try:
        url = "https://www.googleapis.com/youtube/v3/videos"
        page_token = None  # Start with no page token

        while True:
            parameters = {'id': video_id, 'part': 'snippet,statistics'}
            params = {**parameters, 'key': YOUTUBE_API_KEY, 'page_token': page_token}
            response = requests.get(url, params)

            
            payload = json.loads(response.text)
            yield from payload['items']

            page_token = payload.get('nextPageToken')
            if page_token is None:
                break

    except Exception as e:
        print(f"An error occurred: {e.resp.status} {e.content}")
        return None

def youtube_playlist_items(video_id):

    try:
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        page_token = None  # Start with no page token

        while True:
            parameters = {'playlistId': playlist_id, 'part': 'snippet,contentDetails'}
            params = {**parameters, 'key': YOUTUBE_API_KEY, 'page_token': page_token}
            response = requests.get(url, params)

            
            payload = json.loads(response.text)
            yield from payload['items']

            page_token = payload.get('nextPageToken')
            if page_token is None:
                break

    except Exception as e:
        print(f"An error occurred: {e.resp.status} {e.content}")
        return None

def kafka_stream(video):

    video_res = {
        'title': video['snippet']['title'],
        'likes': int(video['statistics'].get('likeCount', 0)),
        'comments': int(video['statistics'].get('commentCount', 0)),
        'views': int(video['statistics'].get('viewCount', 0)),
        'favorites': int(video['statistics'].get('favoriteCount', 0)),
        'thumbnail': video['snippet']['thumbnails']['default']['url']
    }

    producer.send('youtube_videos', json.dumps(video_res).encode('utf-8'),
                          key=video_id.encode('utf-8'))
    # producer.flush()

    print('Sent ', video['snippet']['title'])

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    playlist_id = PLAYLIST_ID
    
    results = youtube_playlist_items(playlist_id)

    if results:
        for video_item in results:
            video_id = video_item['contentDetails']['videoId']
            
            videos = youtube_video_statistics(video_id)
            if videos:
                for video in videos:
                    kafka_stream(video)
            else:
                print("Failed to retrieve data.")
             
    else:
        print("Failed to retrieve data.")