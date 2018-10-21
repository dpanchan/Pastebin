#!/usr/local/bin/python3.6
from flask import Flask
from flask import render_template, redirect, request
import random as r
import string
import os

app = Flask(__name__)

uploads_dir = os.path.join(os.getcwd(), "uploads")
length_of_id = 7
id_chars = string.digits + string.ascii_letters

@app.route("/paste/<paste_id>", methods=['GET'])
def get_paste(paste_id):
  return render_template("200.html", paste=)

@app.route("/", methods=['POST', 'GET'])
def post_paste():
  method = request.method
  if method == "GET":
    return render_template("home.html")
  elif method == "POST":
    paste_id = store(request.body)
    return redirect("/paste/{}".format(paste_id))
  else:
    return render_template("405.html")

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
  
def read_paste()
    
app.run(
    debug=True,
    host='0.0.0.0',
    port=10000
)