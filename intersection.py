
print(".......................Through cosine similarity........................")
import cosinesim
print("\n.....................Through knn................")
import knnfinal
import pandas as pd


# The system shall authenticate user credentials to view the profile
def intersect(list1,list2):
	list3= [value for value in list1 if value in list2]
	return list3
status = "************* Your Recommendations ***************"
print (status)

list1=knnfinal.b
list2=cosinesim.req_index
list3= [value for value in list1 if value in list2]
list1=[]
for i in list3:
	
	list1.append(knnfinal.data_copy.iloc[i].values)
	# print(list1)
	i=i+1
df=pd.DataFrame(list1,columns=['Id','Requirements','project category','Requirement Category','Magnitude of Risk','Impact','Priority'])
df.to_csv("intersect.csv",index=False)
print(df)
#print(x.get_string(fields=["Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]))



