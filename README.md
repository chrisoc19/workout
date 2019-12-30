# Workout
This is a CRUD application, showcasing skills I have picked up whilst working with Python. The main point of this project is to showcase my understanding of CRUD operations and knowledge of the Flask framework.
## Milestone Project 3
## UX
My wire frames were created in Balsamiq and can be found here:

LINK MISSING

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
- Feature 7 - Add a Exercise - On the Add a exercise page, The user is met with a form with three sections, A drop down menu where the user can choose which body part they want to add an exercise for, A short section to give the Exercise a name and a bigger section to add an exercise description. At the bottom of the form there is a submitbutton which adds the exercise to the database.
- Feature 8 - Exercises - Once a User adds a workout they are displayed in a Materializecss Card and shows the Body part name it is realated to, the Username of who added it, the exercise name and the description. There are too buttons an edit and delete button.
- Feature 9 - Edit an Exercise - If the user clicks on the edit button at the bottom of every exercise, they are taken to the edit workout page which has a form similar to Add a workout, the difference is that the edit form comes with some information already added as the user is updating an exercise not creating a new exercise.
- Feature 10 - Delete an Exercise - If the user clicks on the delete button at the bottom of every exercise. A pop up message with a confirm button appears and if the user clicks ok the exercise is then removed from the database.
- Feature 11 - Stop watch - On the Stop watch page, There is a simple javascript counter which the user can start, stop and reset the timer. I added this so the user can keep track of how long the exercise took to complete.
- Feature 12 - Log out - If the user clicks on login/out in the nav bar it removes the session user redirects to the login page. The user then must log back in to access the site.
### Features Left to Implement
- In the future I would like to add User restrictions, For example if the Session User is not the same as the user who added the exercise then that user will not be able to edit or delete the exercise.

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

if __name__ == '__main__':

    app.secret_key = 'super secret key'

    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)

As this enables the user to see any potential bugs on the site and exploit this. Environment variables were stored in env.py  and I used .gitignore to prevent malicious coders from exploiting my database.

### Deploying Locally
    1. Git Clone this application into an IDE or onto a workspace on your computer.
    2. Ensure python3 and pip are installed on your machine
    3. Run $ pip3 install -r requirements.txt.
    4. Create a mongodb username and login. Create yourself a database and a cluster to start using the information on the application.
    5. Modify your env.py with your mongodb username + Password in MONGO_DBNAME and MONGO_URI
    You now have access to the database, the app should be able to run through any data you give it as long as the routing is correct.


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

