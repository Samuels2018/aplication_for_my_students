""" register users """
from db import *
from helpers import *
from register.register_conn import *
import bcrypt
salt = bcrypt.gensalt()
connection = startup_db()


def register_user ():
  """ funtion to register a user """
  name = input("Enter name: ")
  email = input("Enter email: ")
  username = input("Enter username: ")
  password = input("Enter password: ")
  confirm_password = input("Confirm password: ")
  role = input("Enter role: ")

  # validamos que ele email sea valido
  # osea que cumpla con cirtas caracteristicas
  if not validate_email(email):
    print("Invalid email")
    return -1
  
  conn = RegisterConnection(connection)
  existen_user = conn.register_user(email, username)
  if existen_user == -1:
    print("User already exists")
    return -1
  
  # en criptamos la contraseña
  hashed_password = bcrypt.hashpw(password, salt)

  # comparamos la contraseña con la confirmación con la contraseña encriptada
  if bcrypt.checkpw(confirm_password, hashed_password):
    new_user = conn.register_user(name,email,username, hashed_password, role)
    if new_user == -1:
      print("Error registering user")
      return -1
    
    print("User registered")