import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Load music data sheet
music= pd.read_csv("test.csv")
#print(music)


#Select desired features

features= music[["acousticness","danceability", "energy","instrumentalness","loudness","speechiness","tempo","valence"]]
#kompa has the label 1 and is therefore chosen
kompa= music["label"]


#Perform train, test split

training_features, test_features, training_labels, test_labels= train_test_split(features, kompa)

#Scale the feature data so it has mean=0 and standard deviation of 1

scaler=StandardScaler()
training_features=scaler.fit_transform(training_features)
test_features=scaler.transform(test_features)

#Create and train model
model=LogisticRegression()
model.fit(training_features,training_labels)

#Score the model on the train data

score=model.score(training_features,training_labels)

print(score)

#Score the model Test Data
score_test=model.score(test_features,test_labels)
print(score_test)

# Analysze feature coefficients
print(model.coef_)

print(list(zip(["acousticness","danceability", "energy","instrumental","loudness","speechniness","tempo","valence"],model.coef_[0])))


#valence is musical positiveness

#'acousticness', 1.3478807986248316 	MAINLY USE OF STRING INSTRUMENTS

#'energy', 1.0838090968893719			MEAURE OF INTENSITY AND ACTIVITY (FAST, LOUD, NOISY)

#'valence', 1.0810175915818632			MUSICAL POSITIVITY
#-------------------------------------------------------------------------------------------
#'tempo', 0.010578277648573548
#-------------------------------------------------------------------------------------------
#'speechniness', -0.22876947951201837	AMOUNT OF LYRICS USED
		
#'liveness', -0.3904179974335807		WAS THE SONG RECORDED WITH A LIVE AUDIENCE

#'danceability', -0.5309818927149784

#'instrumental', -1.4955828203963273    AMOUNT OF VOCALS IN THE SONG




