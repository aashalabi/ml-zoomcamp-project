
import pickle 
with open('spam_website.bin', 'rb') as f_in:
    dv, model_p = pickle.load(f_in)

# When saving in Windows, use protocol 4
with open('spam_website_p4.bin', 'wb') as f_out:  # Note the 'wb' mode
    pickle.dump((dv, model_p), f_out, protocol=4)  # Use protocol 4 for compatibility


