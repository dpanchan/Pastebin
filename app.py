from flask import Flask
from flask import render_template, redirect
import random as r
import string
import os

app = Flask(__name__)

uploads_dir = os.path.join(os.getcwd(), "uploads")
length_of_id = 8
id_chars = string.digits + string.ascii_letters

@app.route("/<paste_id>", methods=['GET'])
def get_paste(paste_id):
    return generate_paste_id()

@app.route("/upload", methods=['POST'])
def post_paste():
    paste_id = store(request.body)
    return redirect("/paste/{}".format(paste_id))

def store(paste):
    paste_id = generate_paste_id()
    store_path = os.path.join(uploads_dir, paste_id)
    with open(store_path, "w") as f:
        f.write(paste)

def generate_paste_id():
    paste_id = None
    while True:
        paste_id = "".join(r.choices(id_chars, k=length_of_id))    
        if not os.path.isfile(uploads_dir, paste_id):
            break
    return paste_id

app.run(
    debug=True,
    host='0.0.0.0',
    port=10000
)