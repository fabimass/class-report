# Capstone Project: class-report

## Distinctiveness and Complexity
I currently perform as an assistant professor for a university class. This year we have decided that the students will submit their work through GitHub (pretty much inspired on the way that the different projects are submitted for this course). The strategy goes like this:

* We have a repository where every student has a branch with his/her name.
* When a student wants to submit a task, he/she will create a pull request to merge the work into the corresponding branch.
* The last commit in the pull request must have a specific name, because it will be used to identify the submission.  

The problem is that we don't have a quick way to check the progress of each student, we should look into each branch to find the specific commits.

This is why I propose to build a web application where I can quickly see the overall progress of each student for a given class. 

In terms of complexity, the following project will leverage GitHub API to pull the latest data for branches and commits, then it will catalog that information in different Django models, and finally it will show the state of all the submissions for each student. The application has to differentiate between teachers and students in order to adapt the different views accordingly. A lot of work has been put on the look and feel design, using Bootstrap css and also some animations.

Overall, I think this project clearly differentiates from the ones developed during the course, and that it has a fair level of complexity, leveraging Django, Javascript, Bootstrap and APIs, fulfilling the requirements of the capstone project.
<br/>

## Background (further explained)
For each course that we teach, we will create a repository in GitHub. We will also create a branch for each student rolled in the course, these branches will have the same name as the student they represent. Then the students will fork this repository to their own accounts. Whenever they complete a task and want to submit it for review, they will create a commit named specifically as we instruct them (the name of the commit must be exactly the same as the one we provide, else the web app will not recognize it as a proper submission), and then will submit a pull request to merge their work with their assigned branch. After review, the professor will complete the merge and the task will properly count as submitted.
<br/>

## What's in each file

Under submissions folder:

* models.py

    * User: Used for authentication purposes.

    * Sync: This model stores the latest date of synchronization between the application and GitHub. It is automatically populated.

    * Repo: This model stores the references to the GitHub repositories that the application will track. It is manually populated by the professor.

    * Commit: This model stores the names that identify student submissions (the application will ignore commits that do not match any of these names). It is manually populated by the professor.

    * Branch: This model stores all the branches associated to the registered repositories and also which commits were submitted for every branch. It is automatically populated.

    * Pull: This model stores the number of open pull requests for every registered repo.

* admin.py: Here you can find registered the models for Repos and Commits, to let superusers (professors) register new classes and names for submissions.

* urls.py

    * / : The home url will show the list of all repos.
    
    * /<repo_owner>/<repo_name> : Will take you to a page with all the students submissions for the selected repo.
    
    * /login : Takes you to the login page.
    
    * /register : Takes you to the register page.
    
    * /logout : Logout endpoint.
    
    * /sync : This endpoint is used to trigger the synchronization process.

* utils.py: Some utility functions that I use.

    * get_sync_date : Returns the date the last synchronization was made.
    
    * process_branches : Returns an array of all the branches, enriched with the status of each commit and the overall completion.

* views.py

    * index : If a professor is logged in, it will show all the classes. If a student is logged in, it will show only the classes where the student has a branch. If the user is not logged in, it redirects to the login page.

    * submissions : It renders all the branches along with the submissions for a given repo.

    * login_view : Authenticate the user.

    * logout_view : Logs out the user.

    * register : Registers a new user (it will be treated as a student, professors must be superusers).

    * sync_db : It hits the GitHub API to get all the branches, the commits and the pull requests for each repo, then processes the data and updates the given models.

* static/submissions

    * search-branches.js : Used to perform the dynamic search on the list of students.

    * search-repos.js : Used to perform the dynamic search on the list of classes.

    * sync.js : Listens for the click on the sync button and triggers the synchronization process.

    * styles.css : Some custom styles and animations.

* templates/submissions

    * layout.html: It serves as the template for all the pages.

    * index.html: It's the main page, where the list of classes (repos) is displayed.

    * submissions.html: This page shows the progress for each student for a given class.

    * login.html: The login page

    * register.html: Page to register a new user

In the root:

* requirements.txt: This file indicates the required libraries to successfully run the application

* .env: This file is used to inject the Django secret key as an environment variable


## How to run the app

------ Professor ------

Prerequisite: You should have a GitHub repository which will represent a class. You should also create some branches representing each student.

1- Create a super user

2- Log in with your user

3- Click on the Admin button located in the upper right corner

4- Add the reference to the repository in the Repo model. You will need the repo owner and the repo name and, in case the repo is private, you will need also to generate a personal access token.

5- Add some submissions in the Commit model (this will be the name of the expected commits)

6- Return to the home page and hit the Sync button and wait for the process to finish.

7- Click on the class name. You will be taken to the submissions page for that repo. You will see a progress bar for each branch, except the main one (one branch for each student). You will see green checks for those registered commits that exist on each branch, those which do not exist will show a question mark.

8- Click on the branch name to be taken to that specific branch on GitHub.

9- Optionally, use the search bar to find specific branches.


------- Student -------

1- Register (your username should be the same that is going to be use as your branches name)

2- See your progress for each class you are in!