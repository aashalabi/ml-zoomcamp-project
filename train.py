import pandas as pd
import numpy as np

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.tree import export_text
from sklearn.ensemble import RandomForestClassifier

from scipy.io import arff
import pandas as pd

# Load ARFF file
data, meta = arff.loadarff(r'Training Dataset.arff')

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Decode all byte-string columns into int
for column in df.columns:
    if df[column].dtype == 'object':  # Byte strings are usually stored as 'object' dtype
        try:
            df[column] = df[column].str.decode('utf-8').astype(int)  # Decode to regular strings
        except AttributeError:
            pass  # Column doesn't contain byte strings

df.columns = df.columns.str.lower().str.replace(' ', '_')

df_full_train, df_test = train_test_split(df, test_size = 0.2, random_state = 11)
df_train, df_val = train_test_split(df_full_train, test_size = 0.25, random_state = 11)

df_train = df_train.reset_index(drop = True)
df_val   = df_val.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)
df_full_train = df_full_train.reset_index(drop = True)

y_train = df_train.result.values
y_val = df_val.result.values
y_test = df_test.result.values
y_full_train = df_full_train.result.values

del df_train['result']
del df_val['result']
del df_test['result']

X_train = df_train
X_val = df_val
X_test = df_test


dv = DictVectorizer(sparse=False)
X_train_dic = X_train.to_dict(orient='records')
X_train_v = dv.fit_transform(X_train_dic)
rf = RandomForestClassifier(n_estimators=25,
                                    max_depth=10,
                                    random_state=1)

rf.fit(X_train, y_train)

import pickle 

with open('spam_website.bin', 'wb') as f_out:
    pickle.dump((dv, rf), f_out)


