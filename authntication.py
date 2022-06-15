from spotifyData import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Authenticator:

    def __init__(self):
        self.scope = SCOPE
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    def GetSpotifyToken(self):
        return self.sp

    def GetUser(self):

        return self.sp.current_user()
