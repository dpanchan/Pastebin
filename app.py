from flask import Flask
from flask import render_template, redirect, request
from utils import *

app = Flask(__name__)

@app.route("/paste/<paste_id>", methods=['GET'])
def get_paste(paste_id):
  body = read_paste(paste_id)
  if not body:
    abort(404)
  return render_template("200.html", paste=body)

@app.route("/", methods=['POST', 'GET'])
def post_paste():
  method = request.method
  if method == "GET":
    return render_template("home.html")
  elif method == "POST":
    paste_id = store(request.form['paste'])
    return redirect("/paste/{}".format(paste_id))

if __name__ == "__main__":
  check_uploads_folder()
  app.run(
    debug=True,
    host='0.0.0.0',
    port=8080)