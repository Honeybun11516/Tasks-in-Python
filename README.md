Tasks done in Python. The instructions given were:

Requirements
Below are the requirements for this project. There is some functionality already set up in your project. Currently, if you run the program in your VSCode terminal, you will see a menu of options, as shown below:

1. List the tasks
2. Add a task
3. Remove a task
4. Mark a task complete 
5. Quit

What would you like to do?
As the user, you are able to input the number 1 to see all tasks that currently live in the list of tasks (dictionaries) named tasks. The goal here is for you to write the functionality to add, remove, and mark a task complete by inputting 2, 3, or 4, respectively. Instructions are listed below.

Add a Task
Within the already created add_task function, there is a variable named task_text which is the result of the input() function which prompts the user to type in something.
This input() function is a new function that you haven't seen before. It is essentially the opposite of the print() function. This allows for the user to input text when called.

Create a dictionary that uses the task_text variable as the name and sets completed to False.
Add the dictionary to the tasks list.
Within the while loop, add an elif statement that checks if the variable decision (defined within the while loop that allows the user to input a number) is 2, call the add_task function.

Remove a task
You will need a function to handle this.
When this function is run, list out the tasks.
Hint! There is already a function that handles the listing of tasks.

Create a variable that uses input(). The user should be able to input the index number of the task to be removed.
Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.

Write the functionality to be able to delete the task in the list tasks based on the variable you created above.
Within the while loop, add an elif statement that allows your new function to be run when the correct menu option is chosen.

Mark a task complete
You will need a function to handle this.
When this function is run, list out the tasks.
Hint! There is already a function that handles the listing of tasks.

Create a variable that uses input. The user should be able to input the index number of the task to be marked complete.
Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.

Mark the task as complete in the list tasks based on the variable you created above.
Hint! you will need to use two sets of square brackets to find the index and set the appropriate key to True.

Within the while loop, add an elif statement that allows your new function to be run when the correct menu option is chosen.
