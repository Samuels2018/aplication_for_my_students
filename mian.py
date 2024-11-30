""" main file """
from students.students_actions import *
from auth import *
from register import *

def main():
  while True:
    print("1. Login")
    print("2. Register")
    print("3. Create student")
    print("4. Get student")
    print("5. Exit")
    option = input("Enter option: ")

    if option == "1":
      login_user()
    elif option == "2":
      register_user()
    elif option == "3":
      create_student()
    elif option == "4":
      get_student()
    elif option == "5":
      break
    else:
      print("Invalid option")

    ask = input("Do you want to continue? (y/n): ")
    if ask.lower() != "y":
      break