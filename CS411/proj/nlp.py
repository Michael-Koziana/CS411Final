import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re  
import spacy
nlp = spacy.load("en_core_web_sm" )

def funct():
    df = pd.read_json('/Users/michaelkoziana/Desktop/CS411/test.json', lines = True)
    tweets = df['tweet']

    all_sentences = []


    for tweet in tweets:
        all_sentences.append(tweet)


    lines = list()
    for line in all_sentences:    
        words = line.split()
        for w in words: 
            lines.append(w)
            print(w)
            
    lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
    lines2 = []

    for word in lines:
        if word != '':
            lines2.append(word)

    from nltk.stem.snowball import SnowballStemmer
    s_stemmer = SnowballStemmer(language='english')

    stem = []
    for word in lines2:
        stem.append(s_stemmer.stem(word))

    stem2 = []

    for word in stem:
        if word not in nlp.Defaults.stop_words:
            stem2.append(word)

    df = pd.DataFrame(stem2)
    df = df[0].value_counts()

    from nltk.probability import FreqDist

    freqdoctor = FreqDist()

    for words in df:
        freqdoctor[words] += 1
    print(freqdoctor) 

    return df