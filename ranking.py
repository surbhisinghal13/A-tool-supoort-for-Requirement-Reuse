import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
num_req=int(input("Enter the number of Intial requirements"))
requirement=[]
rank=[]
for i in range(num_req):
	req=input("Enter Requirements : ")
	while True:
		try:
			ranking=int(input(" Enter Rank of importance (1-10) :"))
			assert 0< ranking <11
		
		except ValueError:
			print("Not a Number! Enter numbers only !")
		except AssertionError:
			print("Enter a number between 1-10 only!")
		else:
			break
	requirement.append(req)
	rank.append(ranking)
df=pd.DataFrame(np.column_stack([requirement,rank]),columns=['Requirement','Ranking'])
df.to_csv('RankedData.csv',index=False)


	
	
