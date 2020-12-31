import json
import requests

import os
import sys

import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

from secrets import spotify_user_id
from secrets import spotify_token
from secrets import client_id
from secrets import client_secret

from exceptions import ResponseException

class SpotifyFunctionality:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token



    #create playlist and return that playlists id
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Decade",
            "description": "Playlist of specified decade",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

        # the query will tell us where we want to make the post request
        # the request were doing is "create playlist"
        # this request has endpoints which we reference using requests.post()
        # Note: the endpoints are the parameters for post (some parameters optional)
        response = requests.post(
            query,
            data = request_body,
            headers = {
               "Content-Type": "application/json",
               "Authorization": "Bearer {}".format(spotify_token) 
            }
        )

        response_json = response.json()
       
        #response_json.dumps(x, indent=4)
        #print(response_json)

        #playlist id
        return  response_json["id"]

"""
def get_albums(sp):
    saved_albums = list()
    limit = 20
    offset = 0
    results = sp.current_user_saved_tracks(limit, offset)
    counter = results['total']
    
    # loop until no more tracks
    while True:
        for item in results['items']:
            counter = counter - 1
            album = item['album']['track']
            # print("%32.32s %s" % (track['artists'][0]['name'], track['name']))
            saved_albums.append(album)
        if counter == 0:
                break
        offset += 20
        results = sp.current_user_saved_tracks(limit, offset)
    
    return saved_albums
"""

#def filter_by_year(self, year):
    #song_uri_list = get_saved_songs()
    #for i in song_uri_list:
        #if song_uri_list[i]

# search for song given song_name and artist, returns song uri
def get_song_uri(self, song_name, artist):
    query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
        song_name,
        artist
    )
    response = request.get(
        query,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token) 
        }
    )
    resonse_json = response.json()

    songs = response_json["tracks"]["items"]

    # only use the first song
    uri = songs[0]["uri"]

    return uri


# return uri of all current users saved tracks
def get_all_saved_tracks_uris(sp):
    # return value
    saved_tracks = list()
    

    # limit has a maximum of 20
    # offset is the index we start at
    limit = 20
    offset = 0

    # results will get first 20 liked songs
    # counter decremented until there are no more songs (total=0)
    results = sp.current_user_saved_tracks(limit, offset)
    counter = results['total']
    
    # loop until no more tracks
    while True:
        for item in results['items']:
            counter = counter - 1
            track = item['track']
            # print("%32.32s %s" % (track['artists'][0]['name'], track['name']))
            saved_tracks.append(track['uri'])
        if counter == 0:
                break
        offset += 20
        results = sp.current_user_saved_tracks(limit, offset)
    
    return saved_tracks


def main():
    # set scope for functions to get access to specific API endpoints
    scope = 'user-library-read'


    # set auth token 
    # RESET EVERY SO OFTEN: 
    # https://developer.spotify.com/console/get-current-user-saved-tracks/?market=&limit=&offset=
    token = spotify_token


    # set auth_manager and client_credentials_manager
    # these are passed into Spotify() from spotipy library
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    
    auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost:8888/callback', scope=scope)


    # initialize spotipy to work with client
    sp = spotipy.Spotify(auth=token, client_credentials_manager=client_credentials_manager, 
        auth_manager=auth_manager)

    # note that some variables may have arbitrary values (ie. limit=20)
    # this is because client modules (methods) have similar parameters w/ different vals 
    # APPLICATION CODE BELOW

    all_saved_tracks_uris = list()
    all_saved_tracks_albums = list()

    all_saved_tracks_uris = get_all_saved_tracks_uris(sp)
    
    #all_saved_tracks_albums = get_albums(sp)
    #print(all_saved_tracks_albums)
    #album_one = sp.album(all_saved_tracks_uris[0])
    #print(album_one)


if __name__ == '__main__':
    main()

