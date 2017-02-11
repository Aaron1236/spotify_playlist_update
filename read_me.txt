Aaron McKeown: Project Start 2/6/17

INFORMATION SOURCES:
    http://spotipy.readthedocs.io/en/latest/
    https://developer.spotify.com/web-api/code-examples/
    https://developer.spotify.com/web-api/user-guide/
    https://labs.spotify.com/2015/03/09/understanding-spotify-web-api/

    List comprehension
    http://www.secnetix.de/olli/Python/list_comprehensions.hawk

    JSON
    http://docs.python-guide.org/en/latest/scenarios/json/

######################
TO DO # TO DO # TO DO
######################
1. learn about spotipy
1a. sign up
1b. gain authorized access
    1b.a. research
1c. test out each spotipy object. save all tested objects in a reference tab
1d. create list of methods. mark the ones that may be useful.

######################
PROBLEMS # PROBLEMS
######################


######################
IDEAS # IDEAS # IDEAS
######################
 user enters an artist and his/her playlist. if the artist's songs are not in the playlist, then add songs to the playlist
  LIST OF METHODS
  MAIN:
  1. artist_top_tracks(artist_id, country='US')  #Get Spotify catalog information about an artist’s top 10 tracks by country. #Used to get the top songs of the artist
        SCOPE: none

  2. user_playlist_tracks(user, playlist_id=None, fields=None, limit=100, offset=0, market=None) #Get full details of the tracks of a playlist owned by a user.

  3. user_playlist_add_tracks(user, playlist_id, tracks, position=None) #Adds tracks to a playlist
        SCOPE: 'playlist-modify-public'

  4. user_playlist(user, playlist_id=None, fields=None) #Gets playlist of a user Parameters:
        SCOPE: playlist-read-private, playlist-read-collaborative

    USER ENTERS ARTIST ID AND PLAYLIST ID
    PROGRAM COMPARES TOP TRACKS TO SONGS IN GIVEN PLAYLIST
    IF TRACKS ARE NOT IN THE GIVEN PLAYLIST, THEN ADD TRACK TO GIVEN PLAYLIST

    1. create a couple sentence statement that defines the project
add to existing playlist
identify songs by artists x, y, z not in playlist
	a search/compare method will be needed to search for songs. if song is not in playlist, then add song to playlist
		create playlists
		user introduces a list of artists. perhaphs other criteria can be added along with artsists. such criteria could be rating, number of views(you dont want songs with low views. (low views = bad song)),
		identify new songs as by a certain artist
			how to identify whether a song is by a cetain artist. need to check api wrapper.
			include songs where the artist collaborates or song that are only by the artist
		check if new song is not in playlist
			What songs are 'new songs'? will the method go through every song by the artist? or will it try to pre-determine whether a song is new or not before it compares the song to the songs in the playlist. need to check if api wrapper has some kind of filter
			compare the song to all the sng in a playlist
		adding songs to playlists

2. write/drawl out the major steps
3. identify potential obstacles. potential gaps in my knowledge.
4. elaborate on task 2. start identifying the different method that will have to be pieced together.



STEPS:
method 1
the program will use the user playlist method to get a list of the users playlist
the program will ask the user to choose which playlist they want to use.
the user will input the playlist they want
return the playlist id

method 2
user is asked to enter the name of an artist
the search method will return a number of options
the program will provide a list of artists that matched the search.
    the program will associate a number with each artist
the user will input the number accosisacted with the artist they want to choose
return the artist id choosen by the user

method 3
the program will input the choosen artists id into the artist top ten tracks method
the tracks returned by the artists top ten tracks method will be stored in a list
return the list

method 4
the program will input the users choosen playlist id into a method that will return the tracks in the playlist
the track ids of the playlist will be store into a list

method 5
the artists tracks list and the playlist tracks list will be compared.
if any songs are in the artists tracks list but not in the playlist list,
then those song ids will be returned

method 6
add missing songs (return of method 5) to the users playlist
