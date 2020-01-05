import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, jsonify, json, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")


mongo = PyMongo(app)


@app.route('/error')
def error():
    return render_template('error.html')


# Login Page
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['name']})
        bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
        print(request.form['name'])
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = login_user["name"]
                print("Actually got here")
                print(session["username"])
                print(request.form['pass'])
                return redirect(url_for('go_home'))
        flash('Invalid username or password')      
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            print(session['username'])
            print(hashpass)
            return redirect(url_for('go_home'))

        flash('That username already exsits')
    return redirect("login")

# Log out
@app.route('/lo')
def lo():
    try:
        if session["username"]:
            session.clear()
            flash('logout successful')
        return redirect("login")
    except:
        print("No User")
        flash('Please login')
        return redirect("login")

# Home Page
@app.route('/home_page')
def go_home():
    try:
        if session["username"]:
            return render_template("index.html",
                categories=mongo.db.categories.find())
    except:
        print("No User")
    flash('Please login')
    return redirect("login")

# Gets a exercise
@app.route('/get_exercise')
def get_exercise():
    return render_template("exercises.html", exercises=mongo.db.exercise.find())

# Calls the add exercise page
@app.route('/add_exercise')
def add_exercise():
    try:
        if session["username"]:
            categories = mongo.db.categories.find()
            print(session["username"]) 
            return render_template('add_exercise.html', categories=categories)
    except:
        flash('Please login')
        return redirect("login")

        print("no user")

# Adds a exercise to database
@app.route('/insert_exercise', methods=['POST'])
def insert_exercise():
    session_user = (session['username'])
    exercises = mongo.db.exercise
    to_insert = request.form.to_dict()
    to_insert['session_user'] = session_user
    exercises.insert_one(to_insert)

    return redirect(url_for("profile"))


# Updates the database
@app.route('/update_exercise/<exercise_id>', methods=["POST"])
def update_exercise(exercise_id):
    exercise = mongo.db.exercise.find_one({'_id': ObjectId(exercise_id)})
    print(exercise)
    cat = exercise["category_name"]
    cat = cat.lower()
    if cat == "full body":
        cat = "full"
    exercise = mongo.db.exercise
    exercise.update({'_id': ObjectId(exercise_id)}, {
        'category_name': request.form.get('category_name'),
        'exercise_name': request.form.get('exercise_name'),
        'exercise_description': request.form.get('exercise_description'),
        'session_user' : (session['username'])
    })
    return redirect(url_for("profile"))

# Removes exercise from the database for My WORKOUT
@app.route('/delete/<exercise_id>')
def delete(exercise_id):
    exercise = mongo.db.exercise.find_one({'_id': ObjectId(exercise_id)})
    print("finding exercise")
    print(exercise)
    cat = exercise["category_name"]
    cat = cat.lower()
    if cat == "full body":
        cat = "full"
    exercise = mongo.db.exercise
    mongo.db.exercise.delete_one({'_id': ObjectId(exercise_id)})
    if exercise.find({"session_user": session['username']}).count() == 0:
        return redirect(url_for("add_exercise"))
    else:
        flash('Deleted')
        return redirect(url_for("profile"))

# Removes exercise from the database
@app.route('/delete_exercise/<exercise_id>')
def delete_exercise(exercise_id):
    exercise = mongo.db.exercise.find_one({'_id': ObjectId(exercise_id)})
    print(exercise)
    cat = exercise["category_name"]
    cat = cat.lower()
    if cat == "full body":
        cat = "full"
    mongo.db.exercise.delete_one({'_id': ObjectId(exercise_id)})
    flash(' Deleted')
    return redirect(url_for(cat))

# gets all categories
@app.route('/get_categories')
def get_categories():
    try:
        if session["username"]:
            return render_template('categories.html',
                        categories=mongo.db.categories.find())
    except:
        flash('Please login')
        return render_template('login.html')


# Calls the edit exercise page
@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    the_exercise = mongo.db.exercise.find_one({"_id": ObjectId(exercise_id)})
    print(the_exercise)
    all_categories = mongo.db.categories.find()
    return render_template('edit_exercise.html', exercise=the_exercise,
                           categories=all_categories)

# -------------------------------------------- Body workouts

# User profile
@app.route('/profile')
def profile():
    try:
        if session["username"]:
            exercises = mongo.db.exercise
            if exercises.find({"session_user": session['username']}).count() == 0:
                return redirect("add_exercise")
            else:
                return render_template("profile.html", exercises=mongo.db.exercise.find({
                                    "session_user": session['username']}))

    except:
        flash('Please login')
        print("No User")

    return redirect("login")

# Shoulder
@app.route('/shoulders')
def shoulders():
    return render_template("shoulder.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Shoulders"}))

# Grips
@app.route('/grip')
def grip():
    all_users = mongo.db.users.find()
    return render_template("grip.html",  users=all_users,
                           exercises=mongo.db.exercise.find({
                               "category_name": "grips"}))

# Abs
@app.route('/abs')
def abs():
    all_users = mongo.db.users.find()
    return render_template("abs.html",  users=all_users,
                           exercises=mongo.db.exercise.find({
                               "category_name": "Abs"}))

# Arm
@app.route('/arm')
def arm():
    all_users = mongo.db.users.find()
    return render_template("arms.html", users=all_users,
                           exercises=mongo.db.exercise.find({
                               "category_name": "Arm"}))

# Chest
@app.route('/chest')
def chest():
    return render_template("chest.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Chest"}))

# Full Body
@app.route('/full')
def full():
    return render_template("full_body.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Full Body"}))

# Legs
@app.route('/legs')
def legs():
    return render_template("legs.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "legs"}))


# StopWatch Page
@app.route('/watch')
def stop_watch():
    try:
        if session["username"]:
            return render_template("watch.html")
    except:
        flash('Please login')
        return render_template('login.html')
        print("no user")


if __name__ == '__main__':

    app.secret_key = 'super secret key'

    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
