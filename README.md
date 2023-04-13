# Capstone Project: class-report

## Distinctiveness and Complexity
I currently perform as an assistant professor for a university class. This year we have decided that the students will submit their work through GitHub (pretty much inspired on the way that the different projects are submitted for this course). The strategy goes like this:

* We have a repository where every student has a branch with his/her name.
* When a student wants to submit a task, he/she will create a pull request to merge the work into the corresponding branch.
* The last commit in the pull request must have a specific name, because it will be used to identify the submission.  

The problem is that we don't have a quick way to check the progress of each student, we should look into each branch to find the specific commits.

This is why I propose to build a web application where I can quickly see the overall progress of each student for a given class. 

In terms of complexity, the following project will leverage GitHub API to pull the latest data for branches and commits, then it will catalog that information in different models, and finally it will show the state of all the submissions for each student.