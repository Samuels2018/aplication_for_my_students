""" classes for the db connection """
import psycopg2

class RegisterConnection ():
  def __init__(self, connection: psycopg2.extensions.connection):
    self.connection = connection

  def register_user(self, name,email,username, hashed_password, role):
    """
    Register a user
    """
    payload = {
      "name": name,
      "username": username,
      "email": email,
      "password": hashed_password,
      "role": role
    }

    with self.connection.cursor() as cur:
      sql = """
        INSERT INTO users 
        (name, username, email, password, role, createdAt) 
        VALUES (%(name)s, %(username)s, %(email)s, %(password)s , %(role)s, NOW());
      """
      cur.execute(sql, payload)
      return 1
    
    return -1
  
  def get_user(self, username, email):
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