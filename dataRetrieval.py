import spotipy


class DataRetrieval:

    def __init__(self, Spotify):
        self.spotifyToken = Spotify
        self.currently_playing_song = 0
        self.tid = 0
        self.analysis = 0
        self.devices = 0

    def GetCurrentlyPlayingSong(self):
        self.currently_playing_song = self.spotifyToken.currently_playing(
            market="NL")
        return self.currently_playing_song

    def GetSongAnalysis(self):
        self.tid = self.currently_playing_song["item"]["uri"]
        self.analysis = self.spotifyToken.audio_analysis(self.tid)
        return self.analysis
    
    def GetPitches(self):
        for x in self.analysis["segments"]:
            if self.currently_playing_song["progress_ms"] / 1000 < x["start"]:
                return x["pitches"]
    def GetMaxLoudness(self):
        for x in self.analysis["segments"]:
            if self.currently_playing_song["progress_ms"] / 1000 < x["start"]:
                return x["loudness_max"]
            
    def IsPlaying(self):
        self.devices = self.spotifyToken._get("me/player", market=None, additional_types=None)
        return self.devices["is_playing"]

