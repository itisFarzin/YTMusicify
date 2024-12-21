import os
import time
import random
import spotipy
from dotenv import load_dotenv
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi.auth.oauth import OAuthCredentials


load_dotenv()

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

SLEEP_TIME = int(os.getenv("SLEEP_TIME", 5))
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID", None)
YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET", None)
ONLY_THE_FIRST_ARTIST = os.getenv("ONLY_THE_FIRST_ARTIST", "no").lower() == "yes"

if os.getenv("PROXY", None):
    PROXIES = {"https": os.getenv("PROXY")}
else:
    PROXIES = {}


def main():
    ytmusic = YTMusic(
        "youtube.json",
        oauth_credentials=OAuthCredentials(
            client_id=YOUTUBE_CLIENT_ID,
            client_secret=YOUTUBE_CLIENT_SECRET,
            proxies=PROXIES
        ) if YOUTUBE_CLIENT_ID and YOUTUBE_CLIENT_SECRET else None,
        proxies=PROXIES)
    spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="user-library-read",
            proxies=PROXIES
        ),
        proxies=PROXIES
    )

    playlistID = ytmusic.create_playlist(
        "Spotify Liked Music",
        "Created via itisFarzin's YTMusicify"
    )
    if not isinstance(playlistID, str):
        print(f"{RED}Failed to create playlist{RESET}")
        return

    limit = 20
    offset = 0

    results = spotify.current_user_saved_tracks(
        limit=limit,
        offset=offset
    )
    total_liked_songs = results["total"]
    all_liked_songs = []
    all_liked_songs.extend(results["items"])

    while offset + limit < total_liked_songs:
        offset += limit
        results = spotify.current_user_saved_tracks(
            limit=limit,
            offset=offset
        )
        all_liked_songs.extend(results["items"])

    for item in all_liked_songs:
        track = item["track"]
        track_name = track["name"]
        artists_name = (
            track["album"]["artists"][0]["name"] if ONLY_THE_FIRST_ARTIST else 
            ", ".join([artist["name"] for artist in track["album"]["artists"]]))
        try:
            search_results = ytmusic.search(
                track_name + " " + artists_name,
                filter="songs",
                limit=1
            )
            track = search_results[0]
            ytmusic.add_playlist_items(playlistID, [track["videoId"]])
            track_name = track["title"]
            artists_name = ", ".join([artist["name"] for artist in track["artists"]])
            print(f"{GREEN}Added {track_name} by {artists_name} to playlist{RESET}")
        except:
            print(f"{RED}Failed to add {track_name} by {artists_name} to playlist{RESET}")
        time.sleep(int(SLEEP_TIME) + random.randrange(0, 5))

if __name__ == "__main__":
    main()
