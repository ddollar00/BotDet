import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import warnings
import numpy
import re
import os
from sklearn import tree
warnings.filterwarnings("ignore")

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split



def twitPredict():
   
  file= 'training_data_2023.csv'

  training_data = pd.read_csv(file)
  bots = training_data[training_data.bot==1]
  nonbots = training_data[training_data.bot==0]

  filepath = '/home/damion/Desktop/kaggle_data/'
  file= open('training_data_2023.csv', mode='r', encoding='utf-8', errors='ignore')

  training_data = pd.read_csv(file)

  bag_of_words_bot = r'Homework|help|sugar daddy|bot|Bot|tweet me|hacked|follow me|updates every|essay|forget|paypal|logo|nft|crypto|assignment|locked|essays|Maths|Psychology|Writers|' \
          
    #na =false sets nan values to false

  training_data['screen_name'] = training_data.screen_name.str.contains(bag_of_words_bot, case=False, na=False)

  training_data['name'] = training_data.name.str.contains(bag_of_words_bot, case=False, na=False)
  training_data['description'] = training_data.description.str.contains(bag_of_words_bot, case=False, na=False)
  training_data['status'] = training_data.status.str.contains(bag_of_words_bot, case=False, na=False)




  features = ['screen_name', 'name', 'description', 'status', 'verified', 'followers_count', 'friends_count', 'statuses_count',  'bot']

  X = training_data[features].iloc[:,:-1] #iloc gives us row,all column elements except the last one
  y = training_data[features].iloc[:,-1] # iloc gives us row,only the last column element called bot


  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1,random_state=42)

  model = DecisionTreeClassifier(criterion="gini", random_state=42,max_depth=5, min_samples_leaf=10)   
  model.fit(X_train,y_train)


 
  y_pred_train = model.predict(X_train)


  d="%.0f" %(accuracy_score(y_train, y_pred_train)*100)

  file= open('test6.csv', mode='r', encoding='utf-8', errors='ignore')

  data = pd.read_csv(file)
  features = ['screen_name', 'name', 'description', 'status', 'verified', 'followers_count', 'friends_count', 'statuses_count']
  bag_of_words_bot = r'Homework|help|bot|Bot|sugar daddy|tweet me|hacked|follow me|updates every|essay|forget|paypal|logo|nft|crypto|assignment|locked|' \
          
    #na =false sets nan values to false

#data['screen_name'] = data.screen_name.str.contains(bag_of_words_bot, case=False, na=False)
  data['screen_name']= re.search(bag_of_words_bot,str(data.screen_name),re.IGNORECASE).group()==''
  data['name']= re.search(bag_of_words_bot,str(data.name),re.IGNORECASE).group()==''
#data['name'] = data.name.str.contains(bag_of_words_bot, case=False, na=False)

#data['description'] = data.description.str.contains(bag_of_words_bot, case=False, na=False)
  data['description']= re.search(bag_of_words_bot,str(data.description),re.IGNORECASE).group()==''
  data['status']= re.search(bag_of_words_bot,str(data.status),re.IGNORECASE).group()==''
#data['status'] = data.status.str.contains(bag_of_words_bot, case=False, na=False)
  classes=['real','fake']
  test=data[features]
  arr=[classes[model.predict(test)[0]],d]   
  return(arr)
