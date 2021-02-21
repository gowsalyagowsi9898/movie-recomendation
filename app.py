from flask import Flask,request,jsonify, url_for
from flask_cors import CORS
from flask import render_template
import recommendation

app = Flask(__name__)
CORS(app)

@app.route('/movie', methods=['POST'])
def recommend_movies():
    movie_name = request.form['movie_name']
    res = recommendation.results(movie_name)
    return jsonify(res)


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

if __name__=='__main__':
    app.run(port = 5000, debug = True)
