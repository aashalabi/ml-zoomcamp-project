import pickle 
from scipy.io import arff
import pandas as pd
from sklearn.model_selection import train_test_split

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

def predict_single(spam_site, dv, model):
    X = dv.transform([spam_site])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

with open('spam_website.bin', 'rb') as f_in:
    dv, model_p = pickle.load(f_in)

site = X_test.iloc[0].to_dict()

print('Web site example')
print(site)

pred = predict_single(site, dv, model_p)

print('Spam site prediction', pred)

"""
{'having_ip_address': -1,
 'url_length': -1,
 'shortining_service': 1,
 'having_at_symbol': 1,
 'double_slash_redirecting': 1,
 'prefix_suffix': -1,
 'having_sub_domain': 1,
 'sslfinal_state': -1,
 'domain_registeration_length': 1,
 'favicon': 1,
 'port': 1,
 'https_token': 1,
 'request_url': -1,
 'url_of_anchor': -1,
 'links_in_tags': 0,
 'sfh': 1,
 'submitting_to_email': 1,
 'abnormal_url': 1,
 'redirect': 0,
 'on_mouseover': 1,
 'rightclick': 1,
 'popupwidnow': 1,
 'iframe': 1,
 'age_of_domain': -1,
 'dnsrecord': 1,
 'web_traffic': -1,
 'page_rank': -1,
 'google_index': 1,
 'links_pointing_to_page': 1,
 'statistical_report': 1}


"""