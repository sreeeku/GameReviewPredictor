import nltk
from flask import Flask, render_template, url_for, flash, redirect
from forms import RatingForm
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
import re
import numpy as np
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = '10ec2857c5dfee847c6f84a6af7c2058'
rating = '67'


@app.route('/', methods=['POST', 'GET'])
def home():
    form = RatingForm()
    if form.validate_on_submit():
        test_str_copy = form.review.data
        test_str = form.review.data
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        test_str = re.sub(cleanr, '', test_str)
        test_str = re.sub(r"n't", ' not', test_str)
        test_str = re.sub('[^.a-zA-Z\s]', ' ', test_str).strip()
        test_str = test_str.lower()
        text_tokens = word_tokenize(test_str)
        new_stopwords_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
                              "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
                              'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
                              'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
                              'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
                              'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
                              'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
                              'with', 'about', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
                              'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                              'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
                              'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'only', 'own',
                              'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'should',
                              "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'ma', 'shan',
                              "shan't"]
        new_stopwords_dict = dict.fromkeys(new_stopwords_list, None)
        test_str = [word for word in text_tokens if word not in new_stopwords_dict]
        lemmatizer = WordNetLemmatizer()
        test_str = [lemmatizer.lemmatize(word) for word in test_str]
        test_str = " ".join(test_str)
        tfidf_vec = open('models/TFIDF_Vectorizer.p', 'rb')
        tfidf_vec_pickled = pickle.load(tfidf_vec)
        test_vectorizer = TfidfVectorizer(vocabulary=tfidf_vec_pickled.vocabulary_)
        model = open('models/Ridge_Regression_Model.p', 'rb')
        random_forest_model_pickled = pickle.load(model)
        prep_test_vector = test_vectorizer.fit_transform([test_str])
        prediction = round(random_forest_model_pickled.predict(prep_test_vector)[0], 1)
        flash(f'YOUR REVIEW : {test_str_copy}', 'success')
        flash(f'MY MODEL RATING : {prediction}', 'success')
        return redirect(url_for('predict'))
    return render_template('PredictReviewRating.html', form=form)


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('Rating.html', title='Rating', posts=rating)


if __name__ == '__main__':
    app.run(debug=True)
