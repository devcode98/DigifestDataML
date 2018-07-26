import sys
import matplotlib.pyplot as py
import pandas as pd 
import numpy as np 
import Udaipur_guide_data as ud
def func():
    
        
            review_data=pd.read_csv('Guide_review_train.csv')
            i=0
            dict_data=[]  
            while i<40:
                
               temp=str(review_data['Review'][i])
               temp=temp.split(' ')
               var_len=len(temp)
               j=0
               while j< var_len:
                   dict_data.append(temp[j])
                   j=j+1
               i=i+1
            ''' now we have all the words in the seggregrated form '''
            ''' now we will be removing all the duplicates from the data'''
            final_words=[] 
            ''' the above list contains data for the unrepated set of the variables '''
            a=dict_data[0]
            final_words.append(a)
            i=1
            while i<309:
                 a=dict_data[i]
                 if a in final_words:
                     i=i+1
                 else:
                     final_words.append(a)
                     
                 i=i+1
            ''' now we have all the data in the non repetitive nature ,now we can even move to making its sparse matrix 
                as per the data we have but we still have some sort of special characters in it 
                
            
               '''
            more_words=pd.read_csv('wordsbag.csv')   
            more_words=more_words['WORDS']    
            more_words=list(more_words)
            total_words=more_words+final_words   
            ## now we will be making the array for the sparse matrix##
               
            i=0
            j=0
            innerlist=[]
            outerlist=[]
            while i<40:
                j=0
                while j<3120:
                    
                    innerlist.append(0)
                    j=j+1
                outerlist.append(innerlist)    
                innerlist=[]
                i=i+1    
            
            i=0
            j=0
            while i<40:
                  temp=str(review_data['Review'][i])
                  temp=temp.split(' ')
                  var_len=len(temp)
                  j=0
                  while j<var_len:
                     c=0
                     while c<3120:
                         if temp[j]==total_words[c]:
                             outerlist[i][c]=1
                             break
                         else:
                     
                           c=c+1
                     j=j+1
                  i=i+1   
                             
                          
            ''' now we have the sparx matrix ready   '''    
            y_train=pd.read_csv('train_data_review.csv')
            y_train=y_train.iloc[0:,0]
            x_train=pd.DataFrame(outerlist)
            x_train=x_train.iloc[0:,0:]
            
            from sklearn.linear_model import LogisticRegression
            object1= LogisticRegression()
            object1.fit(x_train,y_train)
            test_data=pd.read_csv('test_data.csv')
            list_words_test=str(test_data['Review'])
            # the training data is already ready with us now we will be opening the json files for matching the review#
            
            import json
            # since we can only process a single review at a time we may directly create a list of 3120 items#
            outer_data_list=[]
            i=0
            while i<3120:
                outer_data_list.append(0)
                i=i+1
            new_file=open('online.json','r')
            
            new_file=new_file.readlines()
            new_file=str(new_file[0])
            new_file=new_file.split(' ')   
            str_length=len(new_file)
            
            
            i=0
            j=0
            while i<3120:
                j=0
                while j<str_length:
                    c=0
                    while c<3120:
                       if total_words[c]==new_file[j]:
                           outer_data_list[c]=1
                           c=c+1
                       else:
                         c=c+1   
                    j=j+1
                i=i+1
            
            x_test=pd.DataFrame(outer_data_list)
            x_test=x_test.iloc[0:,0]
            final_array=np.array(x_test)
            final_array=final_array.reshape(1,-1)
            print('done using the logistic regression')
            print(object1.predict(final_array))
            
            
            
            
            
            
            
            from sklearn.naive_bayes import GaussianNB
            gnb = GaussianNB()
            gnb.fit(x_train,y_train)
            print('Using the Naive Bayes')
            print(gnb.predict(final_array))
            
            
            from sklearn.tree import DecisionTreeClassifier
            dec=DecisionTreeClassifier()
            dec.fit(x_train,y_train)
            print('Using the decision tree algorithmn')
            print(gnb.predict(final_array))
            
            from sklearn.ensemble import RandomForestClassifier
            
            rand=RandomForestClassifier()
            rand.fit(x_train,y_train)
            print('Using the Random Forest')
            print(rand.predict(final_array))
            
        
func()
''' Since the data given less is quite less in number it is very much waste of the resources to
    use DEEP LEARNING ALGORITHMNS
'''    