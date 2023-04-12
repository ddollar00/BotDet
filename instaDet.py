import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import warnings
import re
warnings.filterwarnings("ignore")  
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

    
def instaPredict():
        filepath = '/Users/ravendenise/Desktop/BotDet/'
        y_pred_train = model.predict(X_train)
        d="%.0f" %(accuracy_score(y_train, y_pred_train)*100)
	

        file= open('TestingIG2_data - TestingIG_data 1 - in.csv', mode='r', encoding='utf-8', errors='ignore')

        training_data = pd.read_csv(file)

        bag_of_words_bot = r'cash|help|sugar daddy|hacked|follow me|money|essay|forget|paypal|logo|nft|crypto|assignment|locked|sex|play|$|dating|play|relationship|cash app|mama|give away| prizes|hello|support|gmail.com|you|win|winning|lottery|feet|looking for|' \
                  
        def sameDate(c):
            count=0
            for i in c:
                temp=-1
                for j in c:
                    if j.split(" ")[0]==i.split(" ")[0]:
                        temp+=1
                if temp > count:
                    count=temp
            return count
             
            #na =false sets nan values to false
        for i in range(len(training_data)):
            c= (str(training_data.loc[i,"Posts_Dates"]).split("\n"))
            training_data.loc[i,"Username"]= training_data.loc[i,"Username"] not in bag_of_words_bot
            training_data.loc[i,"Bio"]= str(training_data.loc[i,"Bio"]) not in bag_of_words_bot 
            training_data.loc[i,"Posts_Dates"]= (sameDate(c)>=2)
        features = ['Username', 'Number of Posts', 'Followers Count', 'Following Count', 'Bio', 'Verified','Real or Fake']

        X = training_data[features].iloc[:,:-1] #iloc gives us row,all column elements except the last one
        y = training_data[features].iloc[:,-1] # iloc gives us row,only the last column element called bot


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1,random_state=42)

        model = DecisionTreeClassifier(criterion="gini", random_state=42,max_depth=20, min_samples_leaf=20)   
        model.fit(X_train,y_train) 
        y_pred_train = model.predict(X_train)

        d="%.0f" %(accuracy_score(y_train, y_pred_train)*100)

        file= open('userig2.csv', mode='r', encoding='utf-8', errors='ignore')
        training_data = pd.read_csv(file)

        features = ['Username', 'Number of Posts', 'Followers Count', 'Following Count', 'Bio', 'Verified']
        bag_of_words_bot = r'cash|help|sugar daddy|hacked|follow me|money|essay|forget|paypal|logo|nft|crypto|assignment|locked|sex|play|$|relationship|cash app|mama|give away| prizes|hello|support|gmail.com|you|win|winning|lottery|feet|looking for|' \
                  
            #na =false sets nan values to false

        training_data['Username'] =re.search(bag_of_words_bot,str(training_data['Username']),re.IGNORECASE).group()==''
        training_data['Bio'] = re.search(bag_of_words_bot,str(training_data['Bio']),re.IGNORECASE).group()==''


        classes=['real','fake']
        test =training_data[features]

        arr=[classes[model.predict(test)[0]],d]
        return(arr)
instaPredict()