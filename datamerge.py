import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as py

data=pd.read_csv('Udaipur guide data.csv')
data2=pd.read_csv('Udaipur guide data2.csv')
data3=pd.read_csv('Udaipur guide data3.csv')
data4=pd.read_csv('Udaipur guide data4.csv')
data5=pd.read_csv('Udaipur guide data5.csv')
data6=pd.read_csv('Udaipur guide data6.csv')
data7=pd.read_csv('Udaipur guide data7.csv')
list1=data[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list2=data2[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list3=data3[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list4=data4[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list5=data5[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list6=data6[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
list7=data7[['Unnamed: 1','Unnamed: 4','Unnamed: 5']]
listx=list(data['Unnamed: 1'])+list(data2['Unnamed: 1'])+list(data3['Unnamed: 1'])+list(data4['Unnamed: 1'])+list(data5['Unnamed: 1'])+list(data6['Unnamed: 1'])+list(data7['Unnamed: 1'])
listy=list(data['Unnamed: 4'])+list(data2['Unnamed: 4'])+list(data3['Unnamed: 4'])+list(data4['Unnamed: 4'])+list(data5['Unnamed: 4'])+list(data6['Unnamed: 4'])+list(data7['Unnamed: 4'])
listz=list(data['Unnamed: 5'])+list(data2['Unnamed: 5'])+list(data3['Unnamed: 5'])+list(data4['Unnamed: 5'])+list(data5['Unnamed: 5'])+list(data6['Unnamed: 5'])+list(data7['Unnamed: 5'])
udaipur_data1=np.array(listx[0:])
udaipur_data2=np.array(listy[0:])
outerlist=[]
innerlist=[]
i=0
j=0
while i<186:
      innerlist.append(listx[i])
      innerlist.append(listy[i])  
      innerlist.append(listz[i])
      outerlist.append(innerlist)
      innerlist=[]
      i=i+1
final_udaipur_data=pd.DataFrame(outerlist)      