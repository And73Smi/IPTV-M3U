#!/usr/bin/python3
import requests
import sys
import logging

def get_dailymotion_streams(video_id: str):
    """
    Retrieves Dailymotion streams based on the video ID.

    Args:
        video_id (str): The ID of the Dailymotion video.

    Returns:
        None
    """
    try:
        url = f'https://www.dailymotion.com/player/metadata/video/{video_id}'
        response = requests.get(url).json()
        if 'qualities' not in response or not response['qualities']:
            print("No streams available for this video.")
        else:
            stream_url = response['qualities']['auto'][0]['url']
            m3u = requests.get(stream_url).text
            print(m3u)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        sys.exit(1)
    except KeyError as e:
        logging.error(f"Key error: {e}")
        sys.exit(1)
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python dailymotion.py stream")
        sys.exit(1)
    else:
        video_id = sys.argv[1]
        get_dailymotion_streams(video_id)