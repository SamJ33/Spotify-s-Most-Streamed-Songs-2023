import requests
import pandas as pd
import time
import traceback

# Spotify API credentials (replace with your own)
CLIENT_ID = "f4927349dfcf4d3893e33205b0746f5f"
CLIENT_SECRET = "99a2db7d9701427c9ebf4a60c8c8797c        "

# Get Spotify API token
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    response = requests.post(url, {
        'grant_type': 'client_credentials',    
        'client_id': client_id,
        'client_secret': client_secret,
    })
    return response.json().get("access_token")

# Search for a track and get its ID
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    
    try:
        first_result = json_data['tracks']['items'][0]
        return first_result['id'], first_result['external_urls']['spotify']
    except (KeyError, IndexError):
        return None, ""

# Get track details (album cover)
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    try:
        image_url = json_data['album']['images'][0]['url']
        return image_url
    except (KeyError, IndexError):
        return ""

# Load dataset
df = pd.read_csv("spotify-2023.csv", encoding="ISO-8859-1")

token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
track_urls = []
album_cover_urls = []

# Loop through dataset
for index, row in df.iterrows():
    try:
        track_name = row["track_name"]
        artist_name = row["artist(s)_name"]
        print(f"Processing: {track_name} by {artist_name}")
        
        track_id, track_url = search_track(track_name, artist_name, token)
        
        if track_id:
            album_cover_url = get_track_details(track_id, token)
            print(f"✅ Found: {track_url} | Cover: {album_cover_url}")
        else:
            album_cover_url = ""
            print("❌ Not found")
        
        track_urls.append(track_url)
        album_cover_urls.append(album_cover_url)
        time.sleep(0.5)  # To avoid rate limiting
    except Exception as e:
        print("⚠️ Error processing track:", traceback.format_exc())
        track_urls.append("")
        album_cover_urls.append("")

# Add new columns to dataset
df["spotify_track_url"] = track_urls
df["album_cover_url"] = album_cover_urls

# Save updated dataset
output_file = "spotify-2023_with_urls.csv"
df.to_csv(output_file, index=False)
print(f"✅ File saved successfully: {output_file}")
