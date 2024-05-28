import json
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
import os

# Установка переменных окружения
os.environ['SPOTIFY_CLIENT_ID'] = 'ed81911343e4415a86cc4775e8bdc565'
os.environ['SPOTIFY_CLIENT_SECRET'] = 'a252e20e9fdc402bbe706167032d1c9e'

username = '314sgaaqbd53jybxbnsru4njbzyi'
clientID = os.getenv('SPOTIFY_CLIENT_ID')
clientSecret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://localhost:5000/callback'

# Настройка OAuth объекта
oauth_object = SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirect_uri)

# Получение токена доступа
token_info = oauth_object.get_cached_token()
if not token_info:
    token_info = oauth_object.get_access_token()

token = token_info['access_token']
spotifyObject = spotipy.Spotify(auth=token)

# Получение информации о пользователе
try:
    user_name = spotifyObject.current_user()
    print(json.dumps(user_name, sort_keys=True, indent=4))
except Exception as e:
    print(f"Ошибка при получении информации о пользователе: {e}")
    exit(1)

# Основной цикл программы
while True:
    print(f"Welcome to the project, {user_name['display_name']}")
    print("0 - Exit the console")
    print("1 - Search for a Song")
    
    try:
        user_input = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_input == 1:
        search_song = input("Enter the song name: ")
        try:
            results = spotifyObject.search(search_song, 1, 0, "track")
            songs_dict = results['tracks']
            song_items = songs_dict['items']
            if song_items:
                song = song_items[0]['external_urls']['spotify']
                webbrowser.open(song)
                print('Song has opened in your browser.')
            else:
                print("No song found with that name.")
        except Exception as e:
            print(f"Ошибка при поиске песни: {e}")
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")
