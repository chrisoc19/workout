import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'workout_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-fwzhc.mongodb.net/workout_app?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_exercise')
def get_exercise():
    return render_template("exercises.html", exercises=mongo.db.exercise.find())

@app.route('/home_page')
def go_home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)