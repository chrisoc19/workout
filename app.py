import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, jsonify, json, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'workout_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-fwzhc.mongodb.net/workout_app?retryWrites=true&w=majority'

# this above is the Mongo URI


mongo = PyMongo(app)



@app.route('/home_page')
def go_home():
    try:
        if session["username"]:
            return render_template("index.html",
                categories=mongo.db.categories.find()
                )
    except:
        return render_template('login.html')
        print("no user")
    


@app.route('/watch')
def stop_watch():
    try:
        if session["username"]:
            return render_template("watch.html")
    except:
        return render_template('login.html')
        print("no user")

    


# Methods to go into your app.route
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def log_in():
    try:
        if session["username"]:
            print(session["username"])  
    except:
        print("no user")

    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['name']})
        print(login_user["name"])
        print(login_user['password'])
        if login_user:
           
            session['username'] = login_user["name"]
            print("Actually got here")
            print(session["username"])   
            return redirect(url_for('go_home'))

            return 'Invalid username/password combination'
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            print( session['username'])
            return redirect(url_for('go_home'))
        
        return 'That username already exists!'

    return render_template('login.html')

@app.route('/shoulders')
def shoulders():
    return render_template("shoulder.html",
                           exercises=mongo.db.exercise.find({
                               "category_name": "Shoulders"}))


@app.route('/abs')
def abs():
    all_users = mongo.db.users.find()
    return render_template("abs.html",  users=all_users,
                           exercises=mongo.db.exercise.find({
                               "category_name": "Abs"}))



@app.route('/lo')
def lo():
    session.clear()
    return redirect("home_page")



@app.route('/arm')
def arm():
    all_users = mongo.db.users.find()
    return render_template("arms.html", users=all_users,
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
    try:
        if session["username"]:
            session_user = (session['username'])
            categories = mongo.db.categories.find()
            print(session["username"]) 
            return render_template('add_exercise.html', categories=categories)
    except:
        return render_template('login.html')
        print("no user")


@app.route('/insert_exercise', methods=['POST'])
def insert_exercise():
    print(session['username'])
    session_user = (session['username'])
    exercises = mongo.db.exercise
    exercises.insert_one(request.form.to_dict())
    print("added by: " + session_user)
    return render_template("index.html", exercises=mongo.db.exercise.find())
   
   


@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    the_exercise = mongo.db.exercise.find_one({"_id": ObjectId(exercise_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_exercise.html', exercise=the_exercise,
                           categories=all_categories)


@app.route('/update_exercise/<exercise_id>', methods=["POST"])
def update_exercise(exercise_id):
    excercise = mongo.db.exercise.find_one({'_id': ObjectId(exercise_id)})
    cat = excercise["category_name"]
    cat = cat.lower()
    if cat == "full body":
        cat = "full"
    exercise = mongo.db.exercise
    exercise.update({'_id': ObjectId(exercise_id)}, {
        'category_name': request.form.get('category_name'),
        'exercise_name': request.form.get('exercise_name'),
        'exercise_description': request.form.get('exercise_description'),
    })
    return redirect(url_for(cat))


@app.route('/delete_exercise/<exercise_id>')
def delete_exercise(exercise_id):
    excercise = mongo.db.exercise.find_one({'_id': ObjectId(exercise_id)})
    cat = excercise["category_name"]
    cat = cat.lower()
    if cat == "full body":
        cat = "full"
    mongo.db.exercise.remove({'_id': ObjectId(exercise_id)})
    return redirect(url_for(cat))


@app.route('/get_categories')
def get_categories():
    try:
        if session["username"]:
             return render_template('categories.html', 
                           categories=mongo.db.categories.find())
    except:
        return render_template('login.html')
        print("no user")

   


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host=os.environ.get('IP'),
            port=int("3005"),
            debug=True)