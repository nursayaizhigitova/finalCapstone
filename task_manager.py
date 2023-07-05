import os

#Function for user registration.
def reg_user():
    #Here we ask the user for a name, password and password confirmation.
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password == confirm_password:  #Here we check if the passwords match.
        with open("user.txt", "r") as file:
            users = file.readlines()
            existing_users = [user.strip().split(",")[0] for user in users]

        if username.strip() in existing_users:  #Here we check if the user's name already exists.
            print("Error: Username already exists.")
        else:
            with open("user.txt", "a") as file:
                file.write(f"{username},{password}\n")  #Here we write the username and password into the file
            print("The user has been successfully registered.")
    else:
        print("Error: Passwords do not match.")

#Here is the function to add a task.
def add_task():
    assigned_user = input("Enter the name of the user to whom the task has been assigned: ")
    task_title = input("Enter the task title: ")
    task_description = input("Enter a description of the task: ")
    due_date = input("Enter the deadline for the task: ")

    with open("tasks.txt", "a") as file:
        file.write(f"{assigned_user};{task_title};{task_description};{due_date};No\n") #Here we write a task to a file.

    print("The task has been successfully added.")

#Here is a function for viewing all tasks.
def view_all():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    if tasks:  #Here we check if there are any tasks.
        print("List of tasks:")
        for i, task in enumerate(tasks):
            task_data = task.strip().split(",")
            assigned_user = task_data[0]
            task_title = task_data[1]
            task_description = task_data[2]
            due_date = task_data[3]
            task_status = task_data[4]

            print(f"Task {i+1}:")
            print(f"Assigned User: {assigned_user}")
            print(f"Task Title: {task_title}")
            print(f"Task Description: {task_description}")
            print(f"Due Date: {due_date}")
            print(f"Task Status: {task_status}")
            print()
    else:
        print("The task list is empty.")

#Here is a function for viewing user tasks.
def view_mine():
    current_user = input("Enter your username: ")

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    user_tasks = []
    if tasks:
        for task in tasks:
            task_data = task.strip().split(",")
            assigned_user = task_data[0]
            task_title = task_data[1]
            task_description = task_data[2]
            due_date = task_data[3]
            task_status = task_data[4]

            if assigned_user == current_user:  #Here we check if the task belongs to the current user.
                user_tasks.append({
                    "assigned_user": assigned_user,
                    "task_title": task_title,
                    "task_description": task_description,
                    "due_date": due_date,
                    "task_status": task_status
                })

        if user_tasks:
            print(f"List of tasks for the user '{current_user}':")
            for i, task in enumerate(user_tasks):
                task_title = task["task_title"]
                task_description = task["task_description"]
                due_date = task["due_date"]
                task_status = task["task_status"]

                print(f"Task {i+1}:")
                print(f"Task Title: {task_title}")
                print(f"Task Description: {task_description}")
                print(f"Due date: {due_date}")
                print(f"Task Status: {task_status}")
                print()

            user_choice = input("Enter the task number to edit or 'c' to mark a task as complete: ")

            if user_choice.isdigit():
                task_number = int(user_choice) - 1

                if task_number >= 0 and task_number < len(user_tasks):
                    selected_task = user_tasks[task_number]
                    edited_task = edit_task(selected_task)
                    update_task_file(edited_task, tasks)

                    print("The task has been successfully updated.")
                else:
                    print("Error: Invalid task number.")
            elif user_choice.lower() == "c":
                task_number = int(input("Enter the task number to mark as complete: ")) - 1

                if task_number >= 0 and task_number < len(user_tasks):
                    selected_task = user_tasks[task_number]
                    completed_task = mark_task_complete(selected_task)
                    update_task_file(completed_task, tasks)

                    print("The task has been marked as complete.")
                else:
                    print("Error: Invalid task number.")
            else:
                print("Error: Invalid choice.")
        else:
            print(f"The user '{current_user}' has no tasks.")
    else:
        print("The task list is empty.")

#Here is a function for editing tasks.
def edit_task(task):
    print("Editing task...")
    task_title = input("Enter the new task title: ")
    task_description = input("Enter the new task description: ")
    due_date = input("Enter the new due date for the task: ")

    task["task_title"] = task_title
    task["task_description"] = task_description
    task["due_date"] = due_date

    return task

#Here is the function to update the task file.
def update_task_file(task, tasks):
    index = tasks.index(task)
    tasks[index] = f"{task['assigned_user']};{task['task_title']};{task['task_description']};{task['due_date']};{task['task_status']}\n"

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

#Here is the function for marking a task as completed.
def mark_task_complete(task):
    task["task_status"] = "Yes"
    return task

#Here is a function for generating reports.
def generate_reports():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    total_tasks = len(tasks) if tasks else 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    for task in tasks:
        task_data = task.strip().split(",")
        task_status =  task_data[4]

        if task_status == "Yes":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            due_date = task_data [3]
            if due_date < "2023-06-19":
                overdue_tasks += 1
                
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

    with open("task_overview.txt", "w") as file:
        file.write("Task Overview\n")
        file.write(f"Total Tasks: {total_tasks}\n")
        file.write(f"Completed Tasks: {completed_tasks}\n")
        file.write(f"Uncompleted Tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue Tasks: {overdue_tasks}\n")
        file.write(f"Incomplete Percentage: {incomplete_percentage:.2f}%\n")
        file.write(f"Overdue Percentage: {overdue_percentage:.2f}%\n")   
     
    print("The 'task_overview.txt' report has been successfully generated.")
    
    with open("user.txt", "r") as file:
        users = file.readlines()

    total_users = len(users) if users else 0

    with open("user_overview.txt", "w") as file:
        file.write("User Overview\n")
        file.write(f"Total Users: {total_users}\n")
        
        for user in users:
            username = user.strip().split(",")[0]
            user_tasks = [task for task in task if task.strip().split(",")[0] == username]
            user_total_tasks = len(user_tasks)
            user_completed_tasks = sum(1 for task in user_tasks if task.strip().split(",")[4] == "Yes")
            user_incomplete_tasks = user_total_tasks - user_completed_tasks
            user_overdue_tasks = sum(1 for task in user_tasks if task.strip().split(",")[3] < "2023-06-19")

            user_percentage_total_tasks = (user_total_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            user_percentage_completed_tasks = (user_completed_tasks / user_total_tasks) * 100 if user_total_tasks > 0 else 0
            user_percentage_incomplete_tasks = (user_incomplete_tasks / user_total_tasks) * 100 if user_total_tasks > 0 else 0
            user_percentage_overdue_tasks = (user_overdue_tasks / user_incomplete_tasks) * 100 if user_incomplete_tasks > 0 else 0
                
            file.write(f"\nUsername: {username}\n")
            file.write(f"Number of Tasks: {user_total_tasks}\n")
            file.write(f"Percentage of Total Tasks: {user_percentage_total_tasks:.2f}%\n")
            file.write(f"Percentage of Completed Tasks: {user_percentage_completed_tasks:.2f}%\n")
            file.write(f"Percentage of Incomplete Tasks: {user_percentage_incomplete_tasks:.2f}%\n")
            file.write(f"Percentage of Overdue Tasks: {user_percentage_overdue_tasks:.2f}%\n")
        
    print("The 'user_overview.txt' report has been successfully generated.")

def display_statistics():
    print("Displaying statistics...")

def login():
    '''This function reads usernames and passwords from the user.txt file to
    allow a user to login.'''
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")

    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
            return curr_user

    return None

logged_in_user = login()

task_list = []

while True:
    print("Please select one of the following options:")
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("gr - generate reports")
    print("ds - display statistics")
    print("e - exit")

    choice = input("Enter your choice: ")

    if choice == "r":
        reg_user() #Here we call the user registration function.
    elif choice == "a":
        add_task() #Here we call the add task function.
    elif choice == "va":
        view_all() #Here we call the function to view all tasks.
    elif choice == "vm":
        view_mine() #Here we call the user's task view function.
    elif choice == "gr":
        generate_reports() #Here we call the report generation function.
    elif choice == "ds":
        display_statistics()  #Here the function for displaying statistics is called.    
    elif choice == "e":
        print("Exiting the program.")
        break
    else:
        print("Error: Invalid choice. Please try again.")