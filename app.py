from flask import request
from flask import Flask
# create the Flask app
app = Flask(__name__)
#### Boilerplate code - 1 #####
#### Code to load NLP Model and prepare function ####
from keras.preprocessing import sequence
from keras.models import load_model
from keras.preprocessing.text import text_to_word_sequence
from keras.datasets import imdb
from keras.utils import pad_sequences
import numpy as np
# maximum words in each sentence
maxlen = 10
# get the word index from imdb dataset
word_index = imdb.get_word_index()
# load the Model from file
nlp_model = load_model('imdb_nlp.h5')
# method that does the prediction – we will call this later
def predict_sentiment(my_test):
    print('looooooolclear')
    # tokenize the sentence
    word_sequence = text_to_word_sequence(my_test)
    # create a blank sequence of integers
    int_sequence = []
    # for each word in the sentence
    for w in word_sequence:
        # get the integer from vocabulary and add to list
        int_sequence.append(word_index[w])
    # pad the sequence of numbers to input size expected by model
    sent_test = pad_sequences([int_sequence],maxlen=maxlen)
    # make a prediction using our Model
    y_pred = nlp_model.predict(sent_test)
    # return a predicted sentiment real value between 0 and 1
    return y_pred[0][0]
#### Code to load NLP Model and prepare function ####
# build a route or HTTP endpoint
@app.route('/hello')
def hello():
    return 'Hello World!'
##### Code #####
# default HTML to show at first when no input is sent
htmlDefault = '<h4>Simple Python NLP demo</h4><b>Type some text to analyze its sentiment using Deep Learning</b><br><form><textarea rows=10 cols=100 name=\'text_input\'></textarea><br><input type=submit></form>'
# build a route or HTTP endpoint
# this route will read text parameter and analyze it
@app.route('/process')
def process():
    # define returning HTML
    print('ok')
    retHTML = ''
    # get the HTTP parameter by name 'text_input'
    in_text = request.args.get('text_input')
    print(in_text)
    # if input is provided process else show default page
    if in_text is not None:
        # first show what was typed
        retHTML += 'TEXT: <b>%s</b>'%(in_text)
        # run the deep learning Model
        result = predict_sentiment(in_text)
        # if positive sentiment
        if result > 0.5:
        # if negative sentiment
            retHTML += '<h4>Positive Sentiment! :-)</h4><br>'
        else:
            retHTML += '<h4>Negative Sentiment! :-(</h4><br>'
# just show
        return retHTML
    else:
        return htmlDefault
##### New Code #####
#### Boilerplate code - 2 #####
# main application run code
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=1234)
#### Boilerplate code - 2 #####