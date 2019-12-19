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
- Another feature idea

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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The svg body image from the home page was found on  [Code Pen](https://codepen.io/volcanioo/pen/RLXOar)
- The stopwatch was found on [Code Pad](https://codepad.co/snippet/javascript-stopwatch-using-javascript-and-css)
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from [Pixabay](https://pixabay.com/)

### Acknowledgements

- I received inspiration for this project from an iphone app called workout

