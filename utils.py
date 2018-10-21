import random as r
import string
import os

uploads_dir = os.path.join(os.getcwd(), "uploads")
length_of_id = 7
id_chars = string.digits + string.ascii_letters

def get_file_path(path):
  return os.path.join(uploads_dir, path)
  
def store(paste):
  paste_id = generate_paste_id()
  store_path = os.path.join(uploads_dir, paste_id)
  with open(store_path, "w") as f:
    f.write(paste)
  return paste_id

def create_paste_id():
  return "".join(r.choices(id_chars, k=length_of_id))

def generate_paste_id():
  paste_id = create_paste_id()
  store_path = get_file_path(paste_id)
  while os.path.exists(store_path):
    paste_id = create_paste_id()
  return paste_id

def read_paste(paste_id):
  content = None
  with open(get_file_path(paste_id)) as f:
    content = f.read()
  return content


def check_uploads_folder():
  if not os.path.exists(uploads_dir):
    os.mkdir(uploads_dir)