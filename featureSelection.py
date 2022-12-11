# import packages 
import pandas as pd 
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score 
from featurewiz import featurewiz
np.random.seed(1234)

data = pd.read_csv("chessDataFinal.csv")
X = data.drop(['price_range'], axis=1)

y = data.price_range.values

X_scaled =  StandardScaler().fit_transform(X)

X_train, X_valid, y_train, y_valid = train_test_split(X_scaled,y,test_size = 0.2,stratify=y, random_state=1)

classifier = RandomForestClassifier()

classifier.fit(X_train, y_train)

# make prediction
preds = classifier.predict(X_valid)
# check performance
accuracy_score(preds,y_valid)

