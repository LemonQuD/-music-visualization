import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from  spotifyData import *
from pprint import pprint

def write_to_json(result, filename):
    jsonString = json.dumps(result, indent=4)
    jsonFile = open(filename + ".json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def get_song_segment(song_data, progress_s):
    for x in song_data:
        if progress_s < x["start"]:
            return x["pitches"]

# Scope of the Spotify Log In
scope = "user-read-currently-playing"

# Authenticate in Spotify with OAuth 2.0
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

# GE current user
current_user = sp.current_user()
write_to_json(current_user, "source/current_user")

# Retrieve currently playing song
currently_playing_song = sp.currently_playing(market="MD")

# Save the currently playing song data into a JSON file
write_to_json(currently_playing_song, "source/currently_playing_song")

# pprint(currently_playing_song["item"]["uri"])

# Get currently playing song ID from JSON file
tid = currently_playing_song["item"]["uri"]

# Retrive song's audio analysis
analysis = sp.audio_analysis(tid)

# Save the currently playing song's audio analysis into a JSON file
write_to_json(analysis, "source/analysis")

# Get curently playing segment
write_to_json(analysis["segments"], "source/segments")

current_song_pitches = get_song_segment(analysis["segments"], currently_playing_song["progress_ms"] / 1000)
print(current_song_pitches)
