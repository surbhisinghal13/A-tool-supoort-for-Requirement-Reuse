import numpy as np
import pandas as pd 
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import time
from prettytable import PrettyTable


pd.set_option('display.max_colwidth',-1)
# change this to your own path
data1 = pd.read_csv("FinalDataset.csv")
Reqset= pd.read_csv("Rankedbysvm.csv")
data_copy=data1
print(list(data1))
attempts = 5
for attempt in range(attempts):
	try:
		usr_req = Reqset.at[0,'Requirement']
		found=data1.loc[data1['Requirements']==usr_req]
		'''
		id_new=data['ID'].iloc[-1]+1
		df_new=data.append({'ID':id_new,'Requirements':usr_req},ignore_index=True)
		data=df_new
		'''
		
		#found=data[(data.ID==requi.ID)]
		found_req = found['ID']
		#print(found)
		id_target = found_req.tolist()[0]
	except IndexError:
		print ("**** No similar Requirements found ****\nPlease try again")
		# sys.exit(1)
	else:
		print ("************** Seaching Requirement Category *******************")
		break

start_time = time.time()


data1 = pd.concat([data1, pd.get_dummies(data1['project category'])], axis=1)
data1 = pd.concat([data1, pd.get_dummies(data1['Requirement Category'])], axis=1)
data1 = pd.concat([data1, pd.get_dummies(data1['Magnitude of Risk'])], axis=1)
data1 = pd.concat([data1, pd.get_dummies(data1['Impact'])], axis=1)
data1 = pd.concat([data1, pd.get_dummies(data1['Priority'])], axis=1)
data1 = pd.concat([data1, pd.get_dummies(data1['Requirements'])], axis=1)  #now you have a binary variable for each column

req = data1['Requirements']
IDs = data1['ID']

data1 = data1.drop('ID', 1)
data1 = data1.drop('Requirements', 1)
data1 = data1.drop('project category', 1)
data1 = data1.drop('Requirement Category', 1)
data1 = data1.drop('Magnitude of Risk', 1)
data1 = data1.drop('Impact', 1)
data1 = data1.drop('Priority', 1)
data1 = data1.fillna(0)


scaler = MinMaxScaler()

data1 = pd.DataFrame(scaler.fit_transform(data1), columns=data1.columns)

data1['ID'] = IDs  #had to remove this earlier because we didn't want IDs to be scaled with the other columns 

print("Completed in %.3f seconds..." % (time.time() - start_time))

status = "*********** Finding Recommendations ***************"
print (status)
start_time = time.time()

example = data1[data1['ID']==id_target]
example = example.drop('ID', 1)
data1 = data1.drop('ID', 1)


neigh = NearestNeighbors(5)
neigh = neigh.fit(data1)

x = PrettyTable()

x.field_names = ["ID","Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]


output = neigh.kneighbors(example, 5)
a = output[0]
b = output[1]
b=b.flatten().tolist()

for i in b:
	x.add_row(data_copy.iloc[i].values)


print("Completed in %.3f seconds..." % (time.time() - start_time))
print(x.get_string(fields=["Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]))

