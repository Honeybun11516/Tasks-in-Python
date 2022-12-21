from numpy import true_divide


tasks = [
    {'name' : 'Write email to Jan', 'completed' : True},
    {'name' : 'Sweep front porch', 'completed' : True},
    {'name' : 'Call mom', 'completed' : False}
]

def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))

def add_task():
    task_text = input ('Feed the chickens:')
    new_task = {'name' : task_text, 'completed' : False}
    tasks.append(new_task)

def remove_task():
    list_tasks()
    remove_task = int(input('Please enter the number of the task to be removed:'))
    tasks.remove(tasks[remove_task])


def completed_task():
    list_tasks()
    completed_text = int(input('Please enter the number of the task to be completed:'))
    tasks[completed_text]['completed'] = True
    

menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    if decision == '1':
        list_tasks()
    if decision == '2':
        add_task()
    if decision == '3':
        remove_task()
    if decision == '4':
        completed_task()
    elif decision == '5':
        program_is_running = False
    else:
        print('please choose a valid option')
