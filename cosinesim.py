# importing libraries
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from prettytable import PrettyTable

# reading file
data = pd.read_csv('FinalDataset.csv')
Reqset= pd.read_csv("Rankedbysvm.csv")
# checking if we have the right data
print(list(data))

# removing the stop words
req_tfidf = TfidfVectorizer(stop_words='english')
# replace NaN with empty strings
data['Requirements'] = data['Requirements'].fillna('')
# computing TF-IDF matrix required for calculating cosine similarity
data_matrix = req_tfidf.fit_transform(data['Requirements'])

# compuing cosine similarity matrix using linear_kernal of sklearn
cosine_similarity = linear_kernel(data_matrix, data_matrix)

usr_req = Reqset.at[0,'Requirement']
found_req = data[(data.Requirements == usr_req)].index.values.astype(int)[0]


similarity_scores = list(enumerate(cosine_similarity[found_req]))
similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
similarity_scores = similarity_scores[1:6]

# Get the similar req index
req_index = [i[0] for i in similarity_scores]

x = PrettyTable()

x.field_names = ["ID","Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]

# printing the top 5 most similar req using integer-location based indexing (iloc)
for i in req_index:
	# print (data.iloc[i].values)
	x.add_row(data.iloc[i].values)


print(x.get_string(fields=["Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]))
	




