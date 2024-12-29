
import requests
import json
import pickle

model_file_path = r'spam_website_p4.bin'

def load_model(model_path):
    try:
        with open(model_file_path, 'rb') as f_in:
            dv, model = pickle.load(f_in)
    except Exception as e:
        print(f"Error downloading model: {str(e)}")
        raise e

    return(dv, model)
def predict_spam(spam_site, dv, model):
    X = dv.transform([spam_site])
    y_pred = model.predict_proba(X)[0, 1]
    print('input:', spam_site)
    print('output:', y_pred)
    return y_pred


model_tuple = load_model(model_file_path)

def lambda_handler(event, context):

    try:

        # Parse the input data from the event
        if 'body' in event and isinstance(event['body'], str):
            # If the payload is in the 'body' as a string
            X = json.loads(event['body'])['site']
        elif isinstance(event, dict):
            # If the payload is already a dictionary
            X = event['site']
        else:
            # If the payload is a string
            X = json.loads(event)['site']

        dv, model = model_tuple
    
        prediction = predict_spam(X, dv, model)
        spam = prediction >= 0.5
    
        results = {
            'Spam_probability': float(prediction),
            'Spam': bool(spam),
        }

        # Prepare the response
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(results)
        }
        return response
    except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': str(e)
                })
            }


