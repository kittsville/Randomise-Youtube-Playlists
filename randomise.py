from pyyoutube import Api
from random import randint
import requests
import webbrowser
import sys

CLIENT_KEY = sys.argv[1]
CLIENT_SECRET = sys.argv[2]
PLAYLIST_ID = sys.argv[3]

api = Api(client_id=CLIENT_KEY, client_secret=CLIENT_SECRET)

authorization_url = api.get_authorization_url()[0]
webbrowser.open(authorization_url)

authorization_response = input("Provide authorization response")
access_token = api.generate_access_token(authorization_response=authorization_response)

playlist_items_response = api.get_playlist_items(
    playlist_id=PLAYLIST_ID, count=None)

total_items = len(playlist_items_response.items)

print(f'Found {total_items} videos in playlist {PLAYLIST_ID}')

for playlist_item in playlist_items_response.items:
    new_position = randint(0, total_items - 1)

    request_body = {
        "id": playlist_item.id,
        "snippet": {
            "playlistId": PLAYLIST_ID,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": playlist_item.snippet.resourceId.videoId
            },
            "position": new_position
        }
    }

    print(f"Moving video {playlist_item.snippet.resourceId.videoId} to position {new_position}")

    headers = {"Authorization": f"Bearer {access_token.access_token}"}

    update_response = requests.put("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet",  json=request_body, headers=headers)
    
    if update_response.status_code != 200:
        print(update_response.text)
        sys.exit(1)
