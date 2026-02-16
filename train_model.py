import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv('D:/archive (4)/Resume/Resume.csv')

tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(data['Resume_str'])
y = data['Category']

model = LogisticRegression()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))
pickle.dump(tfidf, open("tfidf.pkl","wb"))

print("Model trained")
