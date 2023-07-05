import os

#Here we will ask the user for the number of students registering.
while True:
    try:
        num_students = int(input("Enter the number of students registering: "))
        break
    except ValueError:
        print("Error: Enter a whole number.")

#Here we create a for loop to be executed for each student.
for i in range(num_students):
    #Here we will ask the next student to enter their ID number.
    while True:
        student_id = input("Enter the student ID number: ")
        if student_id.isdigit():
            break
        else:
            print("Error: Enter a number.")

    #Here we will write each ID number into the reg_form.txt file.
    with open("reg_form.txt", "a") as file:
        file.write(f"Student ID: {student_id}\n")
        file.write("--------------------\n")

print("Student registration is now complete.")

#Here we will check if there is a reg_form.txt file.
file_path = "reg_form.txt"
if os.path.isfile(file_path):
    print(f"The {file_path} file exists.")
else:
    print(f"Error: {file_path} file was not found.")

#References:
'''
1. GeeksforGeeks. "Reading and Writing Text Files in Python.": https://www.geeksforgeeks.org/file-handling-python/
    This source proved useful for developing the program as it provided information 
    about reading and writing text files in Python. With the help of this article, 
    I became familiar with the different methods of working with text files, including 
    opening files, reading and writing data, as well as the peculiarities of working with 
    individual strings and characters. This source gave me the necessary knowledge and 
    instructions to properly implement the functionality of the program related to creating 
    and writing data to the "reg_form.txt" file.
'''