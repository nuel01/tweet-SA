# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:51:04 2022

@author: 
"""
import warnings
import joblib

#from sklearn.feature_extraction.text import TfidfVectorizer

#vectorizer=TfidfVectorizer(analyzer="word",lowercase=True)
#tweet = 'We will not waver in our commitment to supporting, equipping and strengthening our Armed Forces, as well as all our security agencies. We will continue investing unprecedented amounts in rebuilding our national security architecture and laying the foundation for a safer Nigeria.'

def predict(tweet):
    
    warnings.warn("user", UserWarning)
    
    tweet = [tweet]
    tagger = joblib.load('vc.joblib2')
    tf = joblib.load('tf.joblib')
    sent = tf.transform(tweet)
    #
    #tweet = vectorizer.fit_transform(tweet)
    #sent = vectorizer.transform(tweet)
    
    pred = tagger.predict(sent)
    if pred == 0:
        return "NEUTRAL"
    elif pred == 1:
        return "POSITIVE"
    else:
        return "NEGATIVE"
#print(pred)