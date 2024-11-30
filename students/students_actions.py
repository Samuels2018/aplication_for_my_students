""" student file """

from db import *
from students.connection_students import *
from helpers import *
connetion = startup_db()


def create_student (): 
  """ function to create a student """
  student_name = input("Enter student name: ")
  student_email = input("Enter student email: ")
  student_phone = input("Enter student phone: ")
  student_age = input("Enter student age: ")
  student_class = input("Enter student class: ")
  admin_id = input("Enter admin id: ")

  # validamos que el usuario tenga permisos
  with connetion.cursor() as cur:
    sql = """
      SELECT role FROM users 
      WHERE id = %(id)s;
    """
    cur.execute(sql, {"id": admin_id})
    role = cur.fetchone()

  if role < 2:
    print("You don't have permission")
    return -1

  # validamos que el email sea valido
  if not validate_email(student_email):
    print("Invalid email")
    return -1

  # buscamos el usuario en la db
  conn = StudentsConnection(connetion)
  student = conn.create_student(student_name, student_email, student_phone, student_age, student_class)
  if student == -1:
    print("Student not found")
    return -1
  
  print("Student created")
  return 1


def get_student ():
  """ function to get a student """
  student_name = input("Enter student name: ")
  student_email = input("Enter student email: ")
  admin_id = input("Enter admin id: ")

  # validamos que el usuario tenga permisos
  with connetion.cursor() as cur:
    sql = """
      SELECT role FROM users 
      WHERE id = %(id)s;
    """
    cur.execute(sql, {"id": admin_id})
    role = cur.fetchone()

  if role < 2:
    print("You don't have permission")
    return -1

  # validamos que el email sea valido
  if not validate_email(student_email):
    print("Invalid email")
    return -1

  # buscamos el usuario en la db
  conn = StudentsConnection(connetion)
  student = conn.get_student(student_name, student_email)
  if student == -1:
    print("Student not found")
    return -1
  
  print(student)
  return 1


def update_student ():
  """ function to update a student """
  student_name = input("Enter student name: ")
  student_email = input("Enter student email: ")
  student_phone = input("Enter student phone: ")
  student_age = input("Enter student age: ")
  student_class = input("Enter student class: ")
  admin_id = input("Enter admin id: ")

  # validamos que el usuario tenga permisos
  with connetion.cursor() as cur:
    sql = """
      SELECT role FROM users 
      WHERE id = %(id)s;
    """
    cur.execute(sql, {"id": admin_id})
    role = cur.fetchone()

  if role < 2:
    print("You don't have permission")
    return -1

  # validamos que el email sea valido
  if not validate_email(student_email):
    print("Invalid email")
    return -1

  # buscamos el usuario en la db
  conn = StudentsConnection(connetion)
  student = conn.update_student(student_name, student_email, student_phone, student_age, student_class)
  if student == -1:
    print("Student not found")
    return -1
  
  print("Student updated")
  return 1


def delete_student ():
  """ function to delete a student """
  student_email = input("Enter student email: ")
  admin_id = input("Enter admin id: ")

  # validamos que el usuario tenga permisos
  with connetion.cursor() as cur:
    sql = """
      SELECT role FROM users 
      WHERE id = %(id)s;
    """
    cur.execute(sql, {"id": admin_id})
    role = cur.fetchone()

  if role < 2:
    print("You don't have permission")
    return -1

  # validamos que el email sea valido
  if not validate_email(student_email):
    print("Invalid email")
    return -1

  # buscamos el usuario en la db
  conn = StudentsConnection(connetion)
  student = conn.delete_student(student_email)
  if student == -1:
    print("Student not found")
    return -1
  
  print("Student deleted")
  return 1


def get_students ():
  """ function to get all students """
  admin_id = input("Enter admin id: ")

  # validamos que el usuario tenga permisos
  with connetion.cursor() as cur:
    sql = """
      SELECT role FROM users 
      WHERE id = %(id)s;
    """
    cur.execute(sql, {"id": admin_id})
    role = cur.fetchone()

  if role < 2:
    print("You don't have permission")
    return -1

  # buscamos el usuario en la db
  conn = StudentsConnection(connetion)
  students = conn.get_students()
  if students == -1:
    print("Students not found")
    return -1
  
  print(students)
  return 1