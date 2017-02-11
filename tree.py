import spotipy
import spotipy.util as util
import pprint

#SAMPLE IDs
#Sample playlist id '23uuakb2NY2aBLJ7fcLPLa'
#sample artist_id = '0EdvGhlC1FkGItLOWQzG4J'
#sample track id = '1yplWxZQqvSg9RRf9FjJm3'

# create method that contains the spotify object and authorization stuff. call on spotify methods. return dicts
class cows:
    def spotify_middle_man(spotify_method, method_info):
        SPOTIPY_CLIENT_ID = '9c6baed919044ddabce6de14a3f26009'
        SPOTIPY_CLIENT_SECRET =
        SPOTIPY_REDIRECT_URI = 'https://localhost:/'
        username = 'deltora555'
        scope = 'playlist-modify-public playlist-modify-private playlist-read-private'
        token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

        if token:
            sp = spotipy.Spotify(auth=token)
            if spotify_method is 'current_user_playlists':
                results = sp.current_user_playlists()#user_playlist_create(username, 'charlie', public=True) #user_playlist_create(user, name, public=True)
                return results
            elif spotify_method is 'artists_top_tracks':
                results = sp.artist_top_tracks(method_info, country='US')
                return results
            elif spotify_method is 'search':
                results = sp.search(q='artist:' + method_info, type='artist')
                return results
            elif spotify_method is 'user_playlist_tracks':
                results = sp.user_playlist_tracks(username, playlist_id=method_info, fields=None) #user_playlist(user, playlist_id=None, fields=None)
                return results
            elif spotify_method is 'user_playlist_add_tracks':
                #results = sp.user_playlist_add_tracks(username, method_info[0], method_info[1], position=None)   #playlist id, tracks
                #['23uuakb2NY2aBLJ7fcLPLa','1yplWxZQqvSg9RRf9FjJm3']
                results = sp.user_playlist_add_tracks(username,method_info[0], [method_info[1]], position=None)
                return results
            elif spotify_method is 'track':
                results = sp.track(method_info)
                return results

            """
            pickle_filename = 'user_playlist_tracks1.pickle'
            pickle_out = open(pickle_filename, 'wb')
            pickle.dump(results, pickle_out)
            pickle_out.close()
            """
        else:
            print ("Can't get token for", username)

    def get_playlist(self):
        """
        method 1
        1the program will use the user playlist method to get a list of the users playlist
        2the program will ask the user to choose which playlist they want to use.
        3the user will input the playlist they want
        4return the playlist id

        """
        method_info = []
        playlist_num = 0
        df = cows.spotify_middle_man('current_user_playlists',method_info)
        # PATHS
        print('Please pick playlist by entering associated number')
        for i in range(len(df['items'])):
            print(df['items'][i]['name'], '   ', i)
        playlist_num = int(input())
        return df['items'][playlist_num]['id']


    def method2(self):
        """
        method 2
        user is asked to enter the name of an artist
        the search method will return a number of options
        the program will provide a list of artists that matched the search.
        the program will associate a number with each artist
        the user will input the number accosisacted with the artist they want to choose
        return the artist id choosen by the user
        """
        artist_num = 0
        method_info = input("please type in the artist's name\n")
        df = cows.spotify_middle_man('search', method_info)
        print("The returned the following artists")
        # artist name
        for i in range(len(df['artists']['items'])):
            print(df['artists']['items'][i]['name'], '   ', i)
        artist_num = int(input('please choose an artist by inputting the associated number\n'))
        print('cool, you have choosen', df['artists']['items'][artist_num]['name'])
        return df['artists']['items'][artist_num]['id']

    def method3(artist_id):
        """
        method 3
        the program will input the choosen artists id into the artist top ten tracks method
        the tracks returned by the artists top ten tracks method will be stored in a list
        return the list
        """
        track_list = []
        df = cows.spotify_middle_man('artists_top_tracks', artist_id)
        for i in range(len(df['tracks'])):
            track_list.append(df['tracks'][i]['id'])
        return track_list

    def method4(playlist_id):
        """
        method 4
        the program will input the users choosen playlist id into a method that will return the tracks in the playlist
        the track ids of the playlist will be store into a list
        """
        track_list = []
        df = cows.spotify_middle_man('user_playlist_tracks', playlist_id)
        for i in range(len(df['items'])):
            track_list.append(df['items'][i]['track']['id'])
        return track_list

    def method5(artist_track_list, playlist_track_list):
        """
        method 5
        the artists tracks list and the playlist tracks list will be compared.
        if any songs are in the artists tracks list but not in the playlist list,
        then those song ids will be returned
        """
        d = set(artist_track_list) & set(playlist_track_list)
        e = list(d)
        for i in e:
            artist_track_list.remove(i)
        return artist_track_list

    def method6(playlist_id, tracks):
        """
        method 6
        add missing songs (return of method 5) to the users playlist
        """
        track_list = []
        print('the following tracks have been added to your playlist')
        for i in tracks:
            cows.spotify_middle_man('user_playlist_add_tracks', [playlist_id, i])
            df = cows.spotify_middle_man('track', i)
            print(df['name'])

#PRIMARY STRUCTURE

playlist_id_choosen = cows.get_playlist('self') #asks user to choose playlist, returns id of choosen playlist
artist_id_choosen = cows.method2('self') #asks users to choose artist, returns id of choosen artist
artists_top_tracks = cows.method3(artist_id_choosen)
playlist_tracks_choosen = cows.method4(playlist_id_choosen)
songs_to_be_added = cows.method5(artists_top_tracks, playlist_tracks_choosen)
cows.method6(playlist_id_choosen, songs_to_be_added)
