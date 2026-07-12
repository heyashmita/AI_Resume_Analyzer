import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#load stopwords
stop_words = set(stopwords.words('english'))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):

    #safety check
    if not text:
        return ""
    
    #convert to lowercase
    text = text.lower()

    #remove special characters
    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        text
    )
    
    #remove extra spaces
    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    #tokenization
    words = text.split()

    cleaned_words = []

    for word in words:

        #remove stopwords
        if word not in stop_words:

            #lemmatization
            word = lemmatizer.lemmatize(word)

            cleaned_words.append(word)



    #join words back
    cleaned_text = " ".join(cleaned_words)

    return cleaned_text