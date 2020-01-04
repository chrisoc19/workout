# Workout
This is a CRUD application, showcasing skills I have picked up whilst working with Python. The main point of this project is to showcase my understanding of CRUD operations and knowledge of the Flask framework.
## Milestone Project 3
## UX
My wire frames were created in Balsamiq and can be found here:

LINK MISSING

I choose to design a simple yet elegant site.
The navigation bar is responsive having break points for smaller, medium and large screens. The navigation links disappear on screen width below 992 pixels and a burger menu icon appears top left. When the burger icon is clicked, it brings a side navigation bar across from the left.
When a user first visits the site they are presented with a clean simple login form with a link to a sign up form if they do not have an account. Leaving out a navigation bar and rendering the logo center just above the forms gives an elegant look and great first-impression.


This website is aimed at a few different types of users:

1. Users who want to be able to store an online copy of their own Workout routines.
2. Users who are looking for inspiration from others on what exercises they should do.
3. Users looking to add, change and update the exercises.

- As a user, I want to be able to Log in and out.
- As a user, I want to be able to browse workout exercises.
- As a user, I want to be able to add and edit workouts.
- As a user, I want to be able to delete workout exercises.

## Features
The main Features of this website will be CRUD, so to be able to Create, Read, Update and Delete from an existing database of information. There is also a way for the User to register and login, When a User is logged in the section My Workouts will display any workouts added or edited by that user.

- Feature 1 - The user is met with a Log in form which allows users to login or register for access to site.
- Feature 2 - Once the user is logged in, They can access the rest of the site and are redirected to the Home page.
- Feature 3 - Nav Bar - On the top of the website the User can find a nav bar which is used to navagate to diffrent parts of the site. On moblie it is a dropdown side nav bar.
- Feature 4 - Home page - On the home page the user is met with a svg image of a body which lights up different body parts when hovering over them with the mouse and on click which take the user to that body part section.   
- Feature 5 - Categories - On the Categories page the User is met with diffrent clickable images and on click which take the user to that body part section. This function is similar to the svg imageson the Home page.
- Feature 6 - My Workouts - On the MY Workout page, the User is met with any exercises that User has added or edited. If this page is empty the user is redirected to the Add a workout page.
- Feature 7 - Add a Exercise - On the Add a exercise page, The user is met with a form with three sections, A drop down menu where the user can choose which body part they want to add an exercise for, A short section to give the Exercise a name and a bigger section to add an exercise description. At the bottom of the form there is a submit button which adds the exercise to the database.
- Feature 8 - Exercises - Once a User adds a workout they are displayed in a Materializecss Card and shows the Body part name it is realated to, the Username of who added it, the exercise name and the description. There are too buttons an edit and delete button.
- Feature 9 - Edit an Exercise - If the user clicks on the edit button at the bottom of every exercise, they are taken to the edit workout page which has a form similar to Add a workout, the difference is that the edit form comes with some information already added as the user is updating an exercise not creating a new exercise.
- Feature 10 - Delete an Exercise - If the user clicks on the delete button at the bottom of every exercise. A pop up message with a confirm button appears and if the user clicks ok the exercise is then removed from the database.
- Feature 11 - Stop watch - On the Stop watch page, There is a simple javascript counter which the user can start, stop and reset the timer. I added this so the user can keep track of how long the exercise took to complete.
- Feature 12 - Log out - If the user clicks on login/out in the nav bar it removes the session user redirects to the login page. The user then must log back in to access the site.
### Features Left to Implement
- In the future I would like to add a function that allows other users to add  other users exercises to their profile section "My Workout".
## Database Schema
I chose to use a document-oriented database using [MongoDB](https://www.mongodb.com)for this web application. There are three collections, one called Categories, which holds which parts of the bodies you can add an exercise for, 'Exercise' which holds the exercise details and one  called 'users' to house user account details.
#### Categories
![alt text](https://github.com/chrisoc19/workout/static/imgs/catDB.png  
"recipes_schema")

#### Exercises
![alt text](https://github.com/chrisoc19/workout/static/imgs/exerciseDB.png 
"user_accounts_schema")

#### User Accounts
![alt text](https://github.com/chrisoc19/workout/static/imgs/usersDB.png 
"user_accounts_schema")
## Technologies Used

- [Python](https://www.python.org/)
    - The project uses **Python**.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Materializecss](https://materializecss.com/)
    - The project uses **Materializecss** to reduce the amount of SCSS and CSS coding that is necessary.
- [Google Fonts ](https://fonts.google.com/)
    - The project uses **Google Fonts**for displaying nice UX icons and text styles for the layout in the website.
- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** for the backend on this project, I was considering MySQL but the control panel of MongoDB makes for a more user friendly experience for coding.

-For Additional technologies used please see requirements.txt


## Testing
I conducted testing across different platforms and web browsers in order to make sure the website worked correctly and looked great across each one. I also asked friends and family to test across their own devices and to give me honest opinions and feedback.
### Validation Services
The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)was used to validate CSS.
- [JSHint](https://jshint.com/)was used to validate JavaScript.
- [AmIReponsive](http://ami.responsivedesign.is/?url=https%3A%2F%2Fworkout-app-flask-mongo.herokuapp.com%2F)was used to test the sites responsiveness.

### User Stories Testing
Manual testing was conducted to ensure the user story objectives were achieved.
1. login form:
    1. Go to the "login" page
    2. Try to navigate else where before logging in and verify that a  "Please log in" error message appears.
    3. Try to submit the form with an invalid username or password and verify that a "Invalid username or password" error message appears.
    4. Try to submit the form with all inputs valid and verify a redirect to home page happens.

    register form:
    1. Go to the "login" page.
    2. Try to register a username that is already in use and verify that a  "That username already exsits" error message appears.
    3. Try to submit the form with all inputs valid and verify a redirect to home page happens.


2. Home page:
    1. Go to the "Home" page
    2. Hover the mouse over the body image and verify that each body part changes color.
    3. When the user clicks on a body part it takes you to the page associated with that body part.
   
3. Categories page:
    1. Go to the "Categories" page.
    2. Tested to see that all images have rendered and are clickable.
    3. When the user clicks on a image it takes you to the page associated with that body part.

4. My workout:
    1. Go to the "My workout" page
    2. Test to see if any exercises added or edited by that user are rendered here.
    3. When the user clicks the edit button on an exercise it opens the edit exercise page.
    4. When a User clicks the delete button it removes the exercise from the database.
    5. If "My workouts" is empty the user is redirected to the "Add an exercise page".

5. Add an exercise form:
    1. Go to the "Add an exercise" page.
    2. Try to choose a category and verify that the drop down menu works and the correct categories are rendered as options.
    3. Try to add an exercise name and verify that the user can add an exercise name.
    4. Try to add an exercise description and verify that the user can add an exercise description.
    5. Try to submit the form with any empty fields and confirm an error message appears.
    6. Try to submit and confirm that the exercise has been added to the database.
    7. Confirm user is redirected to the "My workouts" page.
    
6. Edit an exercise form:
    1. Go to an exercise and select the edit button.
    2. Try to choose a category and verify that the drop down menu works and the correct categories are rendered as options.
    3. Try to edit an exercise name and verify that the user can add an exercise name.
    4. Try to edit an exercise description and verify that the user can add an exercise description.
    5. Try to submit the form with any empty fields and confirm an error message appears.
    6. Try to submit and confirm that the exercise has been edited in the database.
    7. Confirm user is redirected to the "My workouts" page.

7. Stopwatch:
    1. Go to the Stopwatch page.
    2. Confirm that the timer starts.
    3. Try to stop the timer and confirm that the time stops.
    4. Try to start the timer and confirm that the timer starts again.
    5. Try to reset the timer and confirm that the time restes to zero.

Manual testing was done on responsiveness of the site and I am pleased with the final result.

## Bugs 
An interesting bug I found was that if the user added an exercise with an empty form this caused the "My workout" page to stop rendering. I got around this by making all fields mandatory.


## Deployment

The project has been deployed on Heroku to host the site, and all git changes can be seen on my github profile. My deployed version will not have the following code:
There are no differences between the deployed version of the project found [here](https://workout-app-flask-mongo.herokuapp.com/) 
and its development version.

#### How to deploy the code locally

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository from [here](https://github.com/chrisoc19/workout).
2. Click on _Clone_ or _download then Download ZIP_. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment. 
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * ````pip3 install -r requirements.txt````
7. Create a secret key and set as environment variable.
    * MacOS and Linux ````export SECRET_KEY=<secret key>````
    * Windows ````set SECRET_KEY=<secret key>````
8. Connect your MongoDB database to the application. If you have not created a MongoDB database please follow the 
instructions under the heading Create a MongoDB account.
    * Set MongoDB URI as environment variable.
        * MacOS and Linux ````export MONGO_URI=<mongo_uri>````
        * Windows ````set MONGO_URI=<mongo_uri>````
    * Create a database and three collections. One called 'Categories', one called 'Exercise' and the third 'users'.
    * Set MongoDB database name as environment variable.
        * MacOS and Linux ````export MONGO_DBNAME=<mongo_DBNAME>````
        * Windows ````set MONGO_DBNAME=<mongo_DBNAME>````
9. Open up a terminal and run ````flask run````.
10. Navigate to the address the terminal returns to view the project.

#### Deploy to Heroku

This project was deployed to Heroku and uses Heroku for its production environment. Instructions are below on how to 
deploy this web application to a production environment in Heroku.


*Git must be installed onto your computer. Instructions for installing Git can be found 
[here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions 
here to download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

***You must have a MongoDB account and database setup. Follow the instructions under the heading Creating a MongoDB account.

1. Open up Heroku and navigate to your dashboard.
2. Select _New_ > _Create New App_ and fill out the details required then hit _Create App_.
3. Select _Settings_ > _Reveal Config Vars_
    * Enter in the following environment variables:
        * SECRET_KEY: secret key
        * MONGO_URI: mongo uri
        * MONGO_DBNAME: mongo dbname
        * IP: 0.0.0.0
        * PORT:	80
4. Download the code from the Github repository [here](https://github.com/AnthonyNicklin/meat-free).
5. Click on _Clone_ or _download then Download ZIP_. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * ````heroku login````
8. Check the app is present.
    * ````heroku apps````
9. A runtime.txt and Procfile have already been created for this project but make sure they are present. If for some 
reason they are not then follow the steps below to create them.
    * Runtime.txt
        * Create a new text file in the root directory of the project and add ‘python-3.6.6’ to the file.
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run ````touch Procfile````.
        * Add the following text to the Procfile ‘web: flask translate compile; gunicorn meat_free:app’.
10. Add a new git remote for Heroku.
    * ````git remote add heroku git@heroku.comYOUR_APP_NAME.git````
11. Push to Heroku.
    * ````git push heroku master````
12. Give Heroku a few minutes to get it all set up and then check the activity logs under Activity tab in your Heroku 
dashboard. 
13. Once the build is complete click on Open App top right to see the project in action.

### MongoDB
#### Create a MongoDB Account

The database used for this application is MongoDB and a free account can be created [here](https://www.mongodb.com/new).

1. Click on _Try Free_ top right
2. In the right hand panel complete the fields and complete verification steps required
3. Click on _Build a New Cluster_.
    * Select your preferred Cloud provider.
    * Select the region you wish to host and be sure to check the region is in the free tier.  
    * Select a Cluster Tier. Again be careful to select a free one if you wish to host this for free.
    * Select any additional settings you wish to set.
    * Give the Cluster a name.
    * Check settings then once happy select _Create Cluster_.
4. Click on _Collections_ > _Create Database_.
    * Give it a name (remember this as you will need the database name for import settings when deploying the code).
5. Click on _Create Collection_.  
    * Create one with a name of ‘recipes’ and another with a name of ‘user_accounts’.
6. Click on the _Overview_ tab then _Connect_.
    * Click on _Connect Your Application_.
    * Select the correct drive and version.
    * Copy and past the Connection String and keep this safe as you will need it for your MONGO_URI variable to deploy 
    the code.
    
## Credits

### Content
- The svg body image from the home page was found on  [Code Pen](https://codepen.io/volcanioo/pen/RLXOar)
- The stopwatch was found on [Code Pad](https://codepad.co/snippet/javascript-stopwatch-using-javascript-and-css)
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- I received inspiration for this project from an iphone app called workout.

### Media
- The photos used in this site were obtained from [Pixabay](https://pixabay.com/)

### Acknowledgements

- I received inspiration for this project from an iphone app called workout

