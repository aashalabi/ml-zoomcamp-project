import pickle
import numpy as np

from flask import Flask, request, jsonify

#linux: use gunicorn
#pip install gunicorn
#gunicorn --bind localhost:9696 app:app 
#in windows 
#pip install waitress 
# waitress-serve --port=9696 app:app
app = Flask('myapp')

model_file_path = r'spam_website_p4.bin'

with open(model_file_path, 'rb') as f_in:
    dv, model = pickle.load(f_in)

def predict_spam(spam_site, dv, model):
    X = dv.transform([spam_site])
    y_pred = model.predict_proba(X)[0, 1]
    print('input:', spam_site)
    print('output:', y_pred)
    return y_pred


@app.route('/predict', methods = ['GET', 'POST'] )
def ping():
    customer = request.get_json()

    prediction = predict_spam(customer, dv, model)
    spam = prediction >= 0.5
    
    result = {
        'Spam_probability': float(prediction),
        'Spam': bool(spam),
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)
