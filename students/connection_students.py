""" classes for the db connection """
import psycopg2

class StudentsConnection ():
  def __init__(self, connection: psycopg2.extensions.connection, role):
    self.connection = connection

  def create_student (self, student_name, student_email, student_phone, student_age, student_class):
    """
    Register a user
    """
    payload = {
      "name": student_name,
      "email": student_email,
      "phone": student_phone,
      "age": student_age,
      "class": student_class
    }

    with self.connection.cursor() as cur:
      sql = """
        INSERT INTO students 
        (name, email, phone, age, class, createdAt)
        VALUES (%(name)s, %(email)s, %(phone)s, %(age)s, %(class)s, NOW());
      """
      cur.execute(sql, payload)
      return 1
    
    return -1
  
  def get_student (self, username, email):
    """
    Get a user
    """
    payload = {
      "username": username,
      "email": email
    }

    with self.connection.cursor() as cur:
      sql = """
        SELECT * FROM users 
        WHERE username = %(username)s AND email = %(email)s;
      """
      cur.execute(sql, payload)
      user = cur.fetchone()
      return user
    
    return -1
  
  def get_students (self):
    """
    Get all students
    """
    with self.connection.cursor() as cur:
      sql = """
        SELECT * FROM students;
      """
      cur.execute(sql)
      students = cur.fetchall()
      return students
    
    return -1
  
  def update_student (self, student_name, student_email, student_phone, student_age, student_class):
    """
    Update a student
    """
    payload = {
      "name": student_name,
      "email": student_email,
      "phone": student_phone,
      "age": student_age,
      "class": student_class
    }

    with self.connection.cursor() as cur:
      sql = """
        UPDATE students 
        SET name = %(name)s, phone = %(phone)s, age = %(age)s, class = %(class)s
        WHERE email = %(email)s; 
      """

      cur.execute(sql, payload)
      return 1
    
    return -1
  
  def delete_student (self, student_email):
    """
    Delete a student
    """
    payload = {
      "email": student_email
    }

    with self.connection.cursor() as cur:
      sql = """
        DELETE FROM students 
        WHERE email = %(email)s;
      """

      cur.execute(sql, payload)
      return 1
    
    return -1