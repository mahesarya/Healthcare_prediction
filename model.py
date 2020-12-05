#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import needed libraries
import numpy as np
import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
import joblib


# In[2]:


pd.set_option('display.max_columns',None)


# In[3]:


df=pd.read_csv("clean_data.csv")
df.head()


# In[4]:


X=df.drop('stroke',axis=1)
y=df.stroke


# In[5]:


# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


# In[6]:


#load the saved model file
model=joblib.load('model.pkl')


# In[61]:


#function for predictions....
def prediction( gender,age,hypertension,heart_disease,ever_married,work_type ,Residence_type,avg_glucose_level,bmi,smoking_status):
    #creating a array for conating columns values of X
    x=np.zeros(len(X.columns))
    #print(x)
    if 'gender_'+gender in X.columns:
        gender_indices=np.where(X.columns=='gender_'+gender)[0][0]
        x[gender_indices]=1
        #print(x)
    x[0]=age
    x[1]=hypertension
    x[2]=heart_disease
    
    if 'ever_married_'+ever_married in X.columns:
        evermarried_indices=np.where(X.columns=='ever_married_'+ever_married)[0][0]
        x[evermarried_indices]=1
        #print(x)
    if 'work_type_'+work_type in X.columns:
        worktype_indices=np.where(X.columns=='work_type_'+work_type)[0][0]
        x[worktype_indices]=1
        #print(x)
    
    if 'Residence_type_'+Residence_type in X.columns:
        resisdenceindices=np.where(X.columns=='Residence_type_'+Residence_type)[0][0]
        x[resisdenceindices]=1
        #print(x)
    
    x[3]=avg_glucose_level
    x[4]=bmi
    
    if 'smoking_status_'+smoking_status in X.columns:
        smokingindices=np.where(X.columns=='smoking_status_'+smoking_status)[0][0]
        x[smokingindices]=1
#         print(x)
        
    return model.predict([x])[0]
    
    
    
    
    
    


# In[77]:


# print(prediction('Female',61,0,0,'Yes','Self-employed','Rural',202.21,28.89,'never smoked'))


# In[ ]:




