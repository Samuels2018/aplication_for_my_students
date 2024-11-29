""" file to validate email """
import re

def validar_email(email):
  regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return re.match(regex, email) is not None