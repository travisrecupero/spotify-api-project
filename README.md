# spotify-api-project

The purpose of this project is to add specific queries to a current users Spotify library. We will use the Spotify API. When there is an appropriate
application, we can make use of Spotipy which will allow us to query Spotify without the complications of API's.

 Future Improvements/Ideas:
  - Create a front-end interface for users to interact with their data
  - Allowing a user to generate a playlist given a specfic decade based off of their currently saved songs
  - Categorize songs by genre, loudness, danceability, and other Spotify-specific attibutes
  
_____________________________________________________________________________________________________________________________________________________
## Features
- Allows programmer to query the current users entire Spotify library by bypassing the API request limit.
    - application.py: `get_all_saved_tracks_uris(sp)`
      
## JSONSamples
  The folders containing `...JSONSamples` are there to examine output of generated JSONS. This will help us with indexing dictionaries. 

## API Token & Secret
To use the program, create a file named `secrets.py` which includes:
  - `spotify_token = ""`
  - `spotify_user_id = ""`
  - `client_id = ""`
  - `client_secret = ""`
