import json
from spotifyData import *
from authntication import Authenticator
from dataRetrieval import DataRetrieval
from dataProcessing import DataProcessing
from viewer import Emulator


def write_to_json(result, filename):
    jsonString = json.dumps(result, indent=4)
    jsonFile = open(filename + ".json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


def get_song_segment(song_data, progress_s):
    for x in song_data:
        if progress_s < x["start"]:
            return x["pitches"]


# Authenticate in Spotify with OAuth 2.0
auth = Authenticator()
spotifyToken = auth.GetSpotifyToken()


# # Get current user
# user = auth.GetUser()
# write_to_json(user, "source/current_user")

# Data Retrieval
dataRetrieval = DataRetrieval(spotifyToken)

# Retrieve currently playing song
currently_playing_song = dataRetrieval.GetCurrentlyPlayingSong()

# # Save the currently playing song data into a JSON file
# write_to_json(currently_playing_song, "source/currently_playing_song")

# Retrive song's audio analysis
analysis = dataRetrieval.GetSongAnalysis()

# # Save the currently playing song's audio analysis into a JSON file
# write_to_json(analysis, "source/analysis")

# # Get curently playing segment
# write_to_json(analysis["segments"], "source/segments")

dataProcessing = DataProcessing()


emulator = Emulator()
song_is_playing = False
while True:
    currently_playing_song = dataRetrieval.GetCurrentlyPlayingSong()
    current_song_pitches = dataRetrieval.GetPitches()
    temp = dataProcessing.ReturnRGB(current_song_pitches)
    emulator.Animate(temp[0], temp[1])
    if dataRetrieval.IsPlaying() == False:
        while True:
            if dataRetrieval.IsPlaying() == True:
                break
