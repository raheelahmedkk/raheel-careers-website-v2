from re import DEBUG
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, Raheel!</p>"
  return render_template('home.html')  

if __name__ == "__main__":
  # print("Im inside the main section")
  app.run(host="0.0.0.0", debug = True)
