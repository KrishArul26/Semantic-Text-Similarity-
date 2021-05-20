from flask import Flask, request, jsonify,render_template,url_for, request

import flask
import cosineSimilarity
from levenshteinDistance import levenshtein


app = flask.Flask(__name__)
#run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predictRoute():
        data = request.json['data']
        sentence1 = data[0]
        sentence2 = data[1]
        predict1 = levenshtein(sentence1,sentence2)
        vector1 = cosineSimilarity.text_to_vector(sentence1)
        vector2 = cosineSimilarity.text_to_vector(sentence2)
        predict2 = cosineSimilarity.get_cosine(vector1,vector2)
    
        return jsonify({ "Levenshtein Distance" : predict1 , "CosineSimilarity" : predict2})


if __name__ == '__main__':
    
    app.run()


