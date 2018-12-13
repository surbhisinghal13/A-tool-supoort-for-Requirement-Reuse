import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer

def main():
	data=pd.read_csv("RankedData.csv")
	from sklearn.feature_extraction.text import TfidfVectorizer
	tfidf = TfidfVectorizer(encoding='latin-1')

	model = LinearSVC()
	X_train, X_test, y_train, y_test = train_test_split(data['Requirement'], data['Ranking'],test_size=0.50, random_state=0)
	model.fit(tfidf.fit_transform(X_train), y_train)
	y_pred = model.predict(tfidf.transform(X_test))
	print(X_train)
	print(y_train.tolist())	
	values=X_test.index;
	print(y_test)
	print(y_pred)
	for i,j in zip(values,y_pred):
		data.iloc[i,data.columns.get_loc('Ranking')]=j
	data=data.sort_values(by='Ranking')
	print(data)
	data.to_csv("Rankedbysvm.csv",index=False)
	
main()
	
	
	
