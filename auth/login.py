""" login file """
import bcrypt
from db import *
from register.register_conn import *
from helpers import *
connetion = startup_db()


def login_user ():
  """ function to login a user """
  email = input("Enter email: ")
  password = input("Enter password: ")

  # validamos que el email sea valido
  if not validate_email(email):
    print("Invalid email")
    return -1

  # buscamos el usuario en la db
  conn = RegisterConnection(connetion)
  user = conn.get_user(email)
  if user == -1:
    print("User not found")
    return -1
  
  if bcrypt.checkpw(password, user['password']):
    print("User logged in")
    return 1
  
  print("Invalid password")
  return -1