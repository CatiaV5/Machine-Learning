import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr #for importing audio
import spotipy


#Source:https://medium.com/@RareLoot/extracting-spotify-data-on-your-favourite-artist-via-python-d58bc92a4330
#To accces authorised Spotify data
from spotipy.oauth2 import SpotifyClientCredentials 

client_id="bf28c409f086426a8796d1a849b3ac03"
client_secret="33855cfa7bec4513875db348cb9d3ab5"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#Spotify Object to access API
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Chose 
zouk1 = "Suzanna Lubrano"
zouk2= "Kaysha"
zouk3= "Kassav'"


kompa1 = "T-Vice"
kompa2= "Djakout Mizik"
kompa3= "Michel Martelly'"

#search query to find artists Spotify IDs

result_zouk1= sp.search(zouk1)
result_zouk2= sp.search(zouk2)
result_zouk3= sp.search(zouk3)

result_kompa1= sp.search(kompa1)
result_kompa2= sp.search(kompa2)
result_kompa3= sp.search(kompa3)

#print(result_zouk1["tracks"]["items"][0])
#print(result_zouk1["tracks"]["items"][0]["artists"])

#print(zouk2)
#print(result_zouk2["tracks"]["items"][0]["artists"])

#print(zouk3)
#print(result_zouk3["tracks"]["items"][0]["artists"])

#Extracting Spotify albums and creating a list for later referencing
#Extract Artist's URI
artist_uri_zouk1= result_zouk1["tracks"]["items"][0]["artists"][0]["uri"]
artist_uri_zouk2= result_zouk2["tracks"]["items"][0]["artists"][0]["uri"]
artist_uri_zouk3= result_zouk3["tracks"]["items"][0]["artists"][0]["uri"]

artist_uri_kompa1= result_kompa1["tracks"]["items"][0]["artists"][0]["uri"]
artist_uri_kompa2= result_kompa2["tracks"]["items"][0]["artists"][0]["uri"]
artist_uri_kompa3= result_kompa3["tracks"]["items"][0]["artists"][0]["uri"]

#Pull all of the artist's albums+
sp_albums_zouk1 = sp.artist_albums(artist_uri_zouk1, album_type='album')
sp_albums_zouk2 = sp.artist_albums(artist_uri_zouk2, album_type='album')
sp_albums_zouk3 = sp.artist_albums(artist_uri_zouk3, album_type='album')

sp_albums_kompa1 = sp.artist_albums(artist_uri_kompa1, album_type='album')
sp_albums_kompa2 = sp.artist_albums(artist_uri_kompa2, album_type='album')
sp_albums_kompa3 = sp.artist_albums(artist_uri_kompa3, album_type='album')
#print(sp_albums_zouk1)

#Store artist's albums names and URIs in separate list
album_names=[]
album_artist=[]
album_uris=[]
album_labels1=[]

album_names2=[]
album_artist2=[]
album_uris2=[]
album_labels2=[]

album_names3=[]
album_artist3=[]
album_uris3=[]
album_labels3=[]

album_names_kompa1=[]
album_artist_kompa1=[]
album_uris_kompa1=[]
album_labels_kompa1=[]

album_names_kompa2=[]
album_artist_kompa2=[]
album_uris_kompa2=[]
album_labels_kompa2=[]

album_names_kompa3=[]
album_artist_kompa3=[]
album_uris_kompa3=[]
album_labels_kompa3=[]

for i in range(len(sp_albums_zouk1["items"])):
	album_names.append(sp_albums_zouk1["items"][i]["name"])
	album_uris.append(sp_albums_zouk1["items"][i]["uri"])
	album_labels1.append("0")

for i in range(len(sp_albums_zouk2["items"])):
	album_names2.append(sp_albums_zouk2["items"][i]["name"])
	album_uris2.append(sp_albums_zouk2["items"][i]["uri"])
	album_labels2.append("0")
#print(album_labels1)
for i in range(len(sp_albums_zouk3["items"])):
	album_names3.append(sp_albums_zouk3["items"][i]["name"])
	album_uris3.append(sp_albums_zouk3["items"][i]["uri"])
	album_labels3.append("0")

for i in range(len(sp_albums_kompa1["items"])):
	album_names_kompa1.append(sp_albums_kompa1["items"][i]["name"])
	album_uris_kompa1.append(sp_albums_kompa1["items"][i]["uri"])
	album_labels_kompa1.append("1")

for i in range(len(sp_albums_kompa2["items"])):
	album_names_kompa2.append(sp_albums_kompa2["items"][i]["name"])
	album_uris_kompa2.append(sp_albums_kompa2["items"][i]["uri"])
	album_labels_kompa2.append("1")

for i in range(len(sp_albums_kompa3["items"])):
	album_names_kompa3.append(sp_albums_kompa3["items"][i]["name"])
	album_uris_kompa3.append(sp_albums_kompa3["items"][i]["uri"])
	##album_labels_kompa3=dict.fromkeys(album_uris_kompa3,0)
	album_labels_kompa3.append("1")

album_names.extend(album_names2+album_names3+album_names_kompa1+album_names_kompa2+album_names_kompa3)
album_uris.extend(album_uris2+album_uris3+album_uris_kompa1+album_uris_kompa2+album_uris_kompa3)
album_labels=[]
album_labels.extend(album_labels1+album_labels2+album_labels3+album_labels_kompa1+album_labels_kompa2+album_labels_kompa3)
#album_labels={}
#album_labels.update(album_labels1)
#album_labels.update(album_labels2)
#album_labels.update(album_labels_kompa1)
#album_labels.update(album_labels_kompa2)
#album_labels.update(album_labels_kompa3)

#Print out Album URIS
#print(album_uris)

#print(album_labels)


#--------------------------------------------------------------------------------------------------------
#Grab songs from each album
#loop through each album and extract key album track data

def albumSongs(uri, value):
	album=uri
	#Creating Dictionary for a specific album
	spotify_albums[album]= {}

	#Create Keys-Values of empty lists inside a nested dictionary for album
	#Create empty list for each item in album
	spotify_albums[album]["album"]=[]
	spotify_albums[album]["track_number"]=[]
	spotify_albums[album]["id"]=[]
	spotify_albums[album]["name"]=[]
	spotify_albums[album]["uri"]=[]
	spotify_albums[album]["label"]=[]

	#Pull Data on album track

	tracks=sp.album_tracks(album)
	#print(album)

	#print(value)
		
		
			
		

	#Loop for each song track in album

	for n in range(len(tracks['items'])): 
		#values= [value]*n
		spotify_albums[album]['album'].append(album_names[album_count])
		spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
		spotify_albums[album]['id'].append(tracks['items'][n]['id'])
		spotify_albums[album]['name'].append(tracks['items'][n]['name'])
		spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])

	#print(len(spotify_albums[album]["track_number"]))
	values= [value]*len(spotify_albums[album]["track_number"])
	#print(values)
	spotify_albums[album]['label']=values
	#print(spotify_albums[album]['label'])
	#hfhfhf
	
	
   

	    


 
    
 

#-------------------------------------------------------------------------------------------------------------------

spotify_albums={}


album_count=0

for i in range(len(album_uris)):
#for i in album_uris:
	#print(i)
	value=album_labels[i]
	k=album_uris[i]
	#print(k)
	
	albumSongs(k,value)
	
	print("Album " +str(album_names[album_count])+ "songs been added to spotify albums dictionary")
	
	#print(album_count)

# Updates album count once all tracks have been added
	album_count+=1
#for album in spotify_albums:
	#for feature in spotify_albums[album]:
		#print(spotify_albums[album][feature])
	

#hhfh
#-----------------------------------------------------------------------------------------------------------------------

# Grab audio features for each song

#storing audio features and analysis data of each album track and append the data into lists representing
#all the music tracks for that album

def audio_features(album):
	#add new key-values to store audio features

	spotify_albums[album]["acousticness"]=[]
	spotify_albums[album]["danceability"]=[]
	spotify_albums[album]["energy"]=[]
	spotify_albums[album]["instrumentalness"]=[]
	spotify_albums[album]["liveness"]=[]
	spotify_albums[album]["loudness"]=[]
	spotify_albums[album]["speechiness"]=[]
	spotify_albums[album]["valence"]=[]
	spotify_albums[album]["tempo"]=[]
	spotify_albums[album]["popularity"]=[]
	#spotify_albums[album]["style"]=[]



	#ADD HERE FOR AUDIO ANALYSIS
	#spotify_albums[album]["popularity"]=[]
	#spotify_albums[album]["popularity"]=[]

	#Create a track counter
	track_count=0
	#print(len(spotify_albums[album]["uri"]))
	#print(len(labels))


	for track in spotify_albums[album]["uri"]:
		features= sp.audio_features(track)
		#analysis=sp.audio_analysis(#enter track id here)

		spotify_albums[album]["acousticness"].append(features[0]["acousticness"])
		spotify_albums[album]['danceability'].append(features[0]['danceability'])
		spotify_albums[album]['energy'].append(features[0]['energy'])
		spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
		spotify_albums[album]['liveness'].append(features[0]['liveness'])
		spotify_albums[album]['loudness'].append(features[0]['loudness'])
		spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
		spotify_albums[album]['tempo'].append(features[0]['tempo'])
		spotify_albums[album]['valence'].append(features[0]['valence'])
		#spotify_albums[album]['style'].append(features[0]['valence'])



		pop=sp.track(track)
		spotify_albums[album]["popularity"].append(pop["popularity"])
		track_count+=1


#------------------------------------------------------------------------------------------------------------

 #Loop through albums extracting audio features and anlsisis data
 #enter random delay every few albums to avoid sending too many requests at spotify api

import time
import numpy as np
sleep_min=2
sleep_max=5
start_time=time.time()
request_count=0

for i in spotify_albums:
 audio_features(i)
 request_count+=1
 if request_count % 5 ==0:
 	print(str(request_count)+" playlists completed")
 	time.sleep(np.random.uniform(sleep_min,sleep_max))
 	print("Loop #: {}".format(request_count))
 	print("Elapsed Time:{} seconds".format(time.time() - start_time))

 #Orangising data into dictionary which can be turned more easily into a dataframe

dic_df={}
 
dic_df["album"]=[]
dic_df["track_number"]=[]
dic_df['id'] = []
dic_df['name'] = []
dic_df['uri'] = []
dic_df['label'] = []
dic_df['acousticness'] = []
dic_df['danceability'] = []
dic_df['energy'] = []
dic_df['instrumentalness'] = []
dic_df['liveness'] = []
dic_df['loudness'] = []
dic_df['speechiness'] = []
dic_df['tempo'] = []
dic_df['valence'] = []
dic_df['popularity'] = []


#print(spotify_albums[album])

for album in spotify_albums:
	for feature in spotify_albums[album]:
		dic_df[feature].extend(spotify_albums[album][feature])
		#print(dic_df[feature])
		#print(len(album))
		#for y in spotify_albums[album]:
			#print(len(y))
			#print(len(y))
			#print(y,":",spotify_albums[album][y])
#print(len(dic_df["album"]))
#print(dict_df)
#print(len(dic_df[feature]["label"]))
#Convert into dataframe
import pandas as pd

df=pd.DataFrame.from_dict(dic_df)

#Removing duplicates
print(len(df))
final_df=df.sort_values("popularity",ascending=False).drop_duplicates("name").sort_index()
print(len(final_df))

#Write to CSV
final_df.to_csv(r"/Users/jana/Downloads/test.csv")





