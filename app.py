from re import DEBUG
from flask import Flask, render_template, jsonify


app = Flask(__name__) 

JOBS = [
    {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Karachi, Pakistan',
      'salary': 'Rs. 10,00,000'
    },
    {
      'id': 2,
      'title': 'Data Scientist',
      'location': 'Karachi, Pakistan',
      'salary': 'Rs. 20,00,000'
    },
    {
      'id': 3,
      'title': 'Web developer',
      'location': 'Remote',
      # 'salary': 'Rs. 8,00,000'
  },
  {
      'id': 4,
      'title': 'Database administrator',
      'location': 'Karachi, Pakistan',
      'salary': 'Rs. 12,00,000'
  },
  {
      'id': 5,
      'title': 'Frontend developer',
      'location': 'Karachi, Pakistan',
      'salary': 'Rs. 12,00,000'
  }
]


@app.route("/")
def hello_world():
    # return "<p>Hello, Raheel!</p>"
  return render_template('home.html', jobs=JOBS, company_name='RRR Technologies')  

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
  # print("Im inside the main section")
  app.run(host="0.0.0.0", debug = True)
