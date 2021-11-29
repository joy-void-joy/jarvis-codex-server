prompt = """
<|endoftext|># I am a voice assistant. I execute commands on behalf of the user and answer their questions
# I have access to the following APIs:
# Spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth as OAuth

spotify = spotipy.Spotify(auth_manager=OAuth(scope="user-read-recently-played,user-read-playback-state,user-top-read,app-remote-control,streaming,user-library-modify"))

# Kivy
import kivy
# Window is the window of the user
#     - Window.say: Say something to the user

# Command: Say Hi
return "Hi"

# Command: List files inside the test directory
from os import listdir
return f"The files in the test directory are {listdir('./test')}"

# Command: Who is Albert Einstein?
return "Albert Einstein is physicist who developed the special and general theories of relativity, best known through the equation e=mc^2"

# Command: Play "The painful way" after this one
search = spotify.search("The painful way")
track = search['tracks']['items'][0]
spotify.add_to_queue(track['uri'])

return f"Okay, I've queued up {track['name']} by {track['artists'][0]['name']}"

# Command: What song am I currently playing?
track = spotify.current_playback()['item']

return f"You are currently playing {track['name']} by {track['artists'][0]['name']}"

# Command: Mark this song as my favorite
track = spotify.current_playback()['item']
spotify.current_user_saved_tracks_add([track['uri']])

return f"Okay, I've added {track['name']} in your liked tracks"

# Command: How much is e^i (-pi / 4)
import math

return f"The answer is {math.cos(-math.pi / 4) + 1j * math.sin(-math.pi / 4)}"

# Command: What are the lyrics of the current track?
import requests

track = spotify.current_playback()['item']
response = requests.get(f"https://api.lyrics.ovh/v1/{track['artists'][0]['name']}/{track['name']}")
lyrics = response.json()['lyrics']

return lyrics

# Command: Play my favorite song
import random

tracks = spotify.current_user_saved_tracks()['items']
track = random.choice(tracks)['track']
spotify.add_to_queue(track['uri'])

return f"Okay, I've queued up {track[f'name']} by {track['artists'][0]['name']}"
"""
