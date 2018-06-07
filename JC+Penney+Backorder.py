
# coding: utf-8

# In[ ]:

# JC PENNEY Backorder Prediction Model


# In[1]:

import pandas as pd

A = pd.read_csv("C:/Users/Harshil/Desktop/637/Kaggle_Training_Dataset_v2.csv")
print(A.head())


# In[2]:

A.isnull().head()


# In[3]:

A.isnull().sum()


# In[4]:

A[A.lead_time.isnull()]


# In[5]:

A.shape


# In[6]:

A.dropna(how='any').shape


# In[7]:

A.dropna(how='all').shape 


# In[11]:

A.dropna(subset=['national_inv','lead_time','in_transit_qty','forecast_3_month','forecast_6_month','forecast_9_month','sales_1_month','sales_3_month','sales_6_month','sales_9_month','min_bank','potential_issue','pieces_past_due','perf_6_month_avg','perf_12_month_avg','local_bo_qty','deck_risk','oe_constraint','ppap_risk','stop_auto_buy','rev_stop','went_on_backorder'], how='all',inplace=False).shape 


# In[12]:

A.shape


# In[13]:

B = A.shape
B


# In[14]:

import numpy as np
B=A.replace(to_replace=-99 , value=np.nan, inplace=False, limit=None, regex=False, method='pad', axis=None)
B


# In[15]:

B.isnull().sum()


# In[16]:

#B.fillna(B.mean(skipna=True))
B['national_inv'].mean(skipna=True)


# In[17]:

B['national_inv']=B['national_inv'].fillna(496.11283953557677)


# In[18]:

B['lead_time'].mean(skipna=True)


# In[19]:

B['lead_time']=B['lead_time'].fillna(7.872267035168343)
B


# In[20]:

B.isnull().sum()


# In[21]:

B['perf_6_month_avg'].mean(skipna=True)


# In[22]:

B['perf_12_month_avg'].mean(skipna=True)


# In[23]:

B['perf_6_month_avg']=B['perf_6_month_avg'].fillna(0.7823811940800672)
B['perf_12_month_avg']=B['perf_12_month_avg'].fillna(0.7769762678715476)


# In[24]:

B.head()


# In[25]:

B.dtypes


# In[23]:

#df_norm = (df - df.mean()) / (df.max() - df.min())
#B['national_inv'] = (B['national_inv']-B['national_inv'].min()) / (B['national_inv'].max() - B['national_inv'].min())


# In[24]:

#B['lead_time'] = (B['lead_time']-B['lead_time'].min()) / (B['lead_time'].max() - B['lead_time'].min())
#B['in_transit_qty'] = (B['in_transit_qty']-B['in_transit_qty'].min()) / (B['in_transit_qty'].max() - B['in_transit_qty'].min())
#B['forecast_3_month'] = (B['forecast_3_month']-B['forecast_3_month'].min()) / (B['forecast_3_month'].max() - B['forecast_3_month'].min())
#B['forecast_6_month'] = (B['forecast_6_month']-B['forecast_6_month'].min()) / (B['forecast_6_month'].max() - B['forecast_6_month'].min())
#B['forecast_9_month'] = (B['forecast_9_month']-B['forecast_9_month'].min()) / (B['forecast_9_month'].max() - B['forecast_9_month'].min())
#B['sales_1_month'] = (B['sales_1_month']-B['sales_1_month'].min()) / (B['sales_1_month'].max() - B['sales_1_month'].min())
#B['sales_3_month'] = (B['sales_3_month']-B['sales_3_month'].min()) / (B['sales_3_month'].max() - B['sales_3_month'].min())
#B['sales_6_month'] = (B['sales_6_month']-B['sales_6_month'].min()) / (B['sales_6_month'].max() - B['sales_6_month'].min())
#B['sales_9_month'] = (B['sales_9_month']-B['sales_9_month'].min()) / (B['sales_9_month'].max() - B['sales_9_month'].min())
#B['min_bank'] = (B['min_bank']-B['min_bank'].min()) / (B['min_bank'].max() - B['min_bank'].min())
#B['pieces_past_due'] = (B['pieces_past_due']-B['pieces_past_due'].min()) / (B['pieces_past_due'].max() - B['pieces_past_due'].min())
#B['perf_6_month_avg'] = (B['perf_6_month_avg']-B['perf_6_month_avg'].min()) / (B['perf_6_month_avg'].max() - B['perf_6_month_avg'].min())
#B['perf_12_month_avg'] = (B['perf_12_month_avg']-B['perf_12_month_avg'].min()) / (B['perf_12_month_avg'].max() - B['perf_12_month_avg'].min())
#B['local_bo_qty'] = (B['local_bo_qty']-B['local_bo_qty'].min()) / (B['local_bo_qty'].max() - B['local_bo_qty'].min())


# In[26]:

B.head()


# In[27]:

B.replace(to_replace='No' , value=0, inplace=True, limit=None, regex=False, method='pad', axis=None)
B.replace(to_replace='Yes' , value=1, inplace=True, limit=None, regex=False, method='pad', axis=None)

#B['deck_risk'].replace(('yes', 'no'), (1, 0), inplace=True)
#B.deck_risk.eq('yes').mul(1)
#B['deck_risk'] = B['deck_risk'].apply(lambda x: 0 if x=='no' else 1)

B.head(20)


# In[28]:

#def normalize(B):
 #   result = B.copy()
B=B.astype(int)
for i in B.columns:
    #B[i] = int(B[i])
    max_value = B[i].max()
    min_value = B[i].min()
    B[i] = (B[i] - min_value) / (max_value - min_value)
  #  return result


# In[29]:

B.head()


# In[30]:

B.dtypes


# In[31]:

B['deck_risk']=B['deck_risk'].astype(int)
B['oe_constraint']=B['oe_constraint'].astype(int)
B['ppap_risk']=B['ppap_risk'].astype(int)
B['stop_auto_buy']=B['stop_auto_buy'].astype(int)
B['rev_stop']=B['rev_stop'].astype(int)
B['went_on_backorder']=B['went_on_backorder'].astype(int)


# In[32]:

B.dtypes


# In[33]:

B.head()


# In[ ]:

import pandas as pd
B.to_csv('C:/Users/Harshil/Desktop/637/backorder1.csv')


# In[7]:

B.to_csv("C:/Users/Harshil/Desktop/637/harshil_norm_withoutNA_dataset.csv")


# In[34]:

del B['sku']


# In[35]:

B.head()


# In[36]:

#from sklearn.model_selection import train_test_split
#X = B.loc[:, B.columns != 'went_on_backorder']
#y = B['went_on_backorder']#
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[2]:

#from sklearn.neighbors import KNeighborsClassifier
#train = B.sample(int(0.7*len(B)))
#test = B[B.apply(lambda x: x.values.tolist() not in train.values.tolist(), axis=1)]
#X1_train, X1_test, Y1_train, Y1_test = X_train.iloc[:100], X_test.iloc[:100], y_train.iloc[:100], y_test.iloc[:100]
import pandas as pd
C = pd.read_csv("C:/Users/Harshil/Desktop/637/harshil_norm_without_NA_dataset.csv")
print(C.head())


# In[3]:

from sklearn.model_selection import train_test_split
X = C.loc[:, C.columns != 'went_on_backorder']
y = C['went_on_backorder']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[10]:

from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train,y_train)

#use hard voting to predict (majority voting)
pred=clf.predict(X_test)
print(pred)
print(accuracy_score(pred,y_test))


# In[6]:

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
clf = RandomForestClassifier(max_depth=600, max_features='log2', min_samples_split=180, random_state=150, n_estimators=2000, criterion='entropy')
clf.fit(X_train,y_train)

#use hard voting to predict (majority voting)
pred=clf.predict(X_test)
print(accuracy_score(pred,y_test))


# In[35]:

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
#clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
clf.fit(X_train,y_train)
pred = clf.predict(X_test)
print("Accuracy Score: ",accuracy_score(pred,y_test))
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


# In[22]:

print("confusion matrix: ")
print(confusion_matrix(y_test,pred))


# In[28]:

print("Classification Report: ")
print(classification_report(y_test,pred))


# In[27]:

C.head(20)


# In[33]:

from datetime import datetime
start_time = datetime.now()
# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
