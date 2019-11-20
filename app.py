import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'workout_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-fwzhc.mongodb.net/workout_app?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home_page')
def go_home():
    return render_template("home.html", 
                           categories=mongo.db.categories.find())


@app.route('/shoulder')
def shoulder():
    return render_template("shoulder.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Shoulders"}))


@app.route('/abs')
def abs():
    return render_template("abs.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Abs"}))


@app.route('/arms')
def arms():
    return render_template("arms.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Arm"}))


@app.route('/chest')
def chest():
    return render_template("chest.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Chest"}))


@app.route('/full')
def full():
    return render_template("full_body.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Full Body"}))


@app.route('/legs')
def legs():
    return render_template("legs.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "legs"}))

@app.route('/get_exercise')
def get_exercise():
    return render_template("exercises.html", exercises=mongo.db.exercise.find())


@app.route('/add_exercise')
def add_exercise():
    categories = mongo.db.categories.find()
    return render_template('add_exercise.html', categories=categories)


@app.route('/insert_exercise', methods=['POST'])
def insert_exercise():
    exercises = mongo.db.exercise
    exercises.insert_one(request.form.to_dict())
    return render_template("home.html", exercises=mongo.db.exercise.find())


@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    the_exercise = mongo.db.exercise.find_one({"_id": ObjectId(exercise_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_exercise.html', exercise=the_exercise,
                           categories=all_categories)


@app.route('/update_exercise/<exercise_id>', methods=["POST"])
def update_exercise(exercise_id):
    exercise = mongo.db.exercise
    exercise.update({'_id': ObjectId(exercise_id)}, {
        'category_name': request.form.get('category_name'),
        'exercise_name': request.form.get('exercise_name'),
        'exercise_description': request.form.get('exercise_description'),
        'is_urgent': request.form.get('is_urgent')
    })
    return redirect(url_for('go_home'))


@app.route('/delete_exercise/<exercise_id>')
def delete_exercise(exercise_id):
    mongo.db.exercise.remove({'_id': ObjectId(exercise_id)})
    return redirect(url_for('go_home'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', 
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
