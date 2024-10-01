import pickle
import pandas as pd
import json
import numpy as np
import joblib
from keras.models import load_model
import tensorflow as tf


# Load the Random Forest model
from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(sentence):
    # Create the TF-IDF vectorizer with the sentence as the only document
    vectorizer = TfidfVectorizer(max_features=8000, ngram_range=(1, 2))
    
    # Fit and transform the data
    tfidf_matrix = vectorizer.fit_transform([sentence])
    
    # Extract TF-IDF values for the given sentence
    tfidf_values = tfidf_matrix.toarray()[0]
    
    # Get feature names (terms)
    terms = vectorizer.get_feature_names_out()
    
    # Create a dictionary to store term and corresponding TF-IDF value
    tfidf_dict = dict(zip(terms, tfidf_values))

    # Print the TF-IDF values for each term in the sentence
 
    
    return tfidf_dict


stop_words = np.load("./stopwords.npy")
punctuation = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~؛؟ُ،ًٌٍَُِّْــ'

def punctuation_delete(sentence):
    return sentence.translate(str.maketrans('', '', punctuation))

def stopwords_delete(text):
    text = ' '.join([i for i in text.split(' ') if i not in stop_words])
    return text

def predict_mpg(config):
    # ##loading the model from the saved file

   pkl_filename = "news_predict.pkl"
#    with open('news_predict.pkl', 'rb') as f:
#     data = pickle.load(f)

#    rf = pd.load(f'./{pkl_filename}')
   
   config = stopwords_delete(config)
   config = punctuation_delete(config)

   list = []
   c = calculate_tfidf(config)
   for term, tfidf_value in c.items():
       list.append(tfidf_value)

#    try:
#     with open(pkl_filename, 'rb') as f_in:
#         model = pickle.load(f_in)
#     print("Model loaded successfully.")
#    except FileNotFoundError:
#     print("File not found. Please check the file path.")
#    except Exception as e:
#     print(f"An error occurred: {e}")
#    print("Doneeeee")

   
   try:
        new_model = tf.keras.models.load_model('my_model.keras')

# Show the model architecture
        print(new_model.summary())
    # model = load_model(pkl_filename) 
    # y_pred = model.predict(c)
    # print(y_pred)
   except Exception as e:
    print(f"Error: {e}")

   return config
 
    # if y_pred == 1:
    #     return 'Science and Culture'
    # elif y_pred == 2:
    #     return 'Sport'
    # elif y_pred == 3:
    #     return 'Economy'
    # elif y_pred == 4:
    #     return 'Miscellaneous'
    # elif y_pred == 5:
    #     return 'Literature and Art'
    # elif y_pred == 6:
    #     return 'Social'
    # elif y_pred == 7:
    #     return 'Politics'
    # elif y_pred == 8:
    #     return 'Tourism'
    # elif y_pred == 9:
    #     return 'Natural Environment'