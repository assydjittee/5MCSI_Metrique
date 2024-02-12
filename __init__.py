from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/contact/")
def contact():
    return render_template("contact.HTML")

@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    minutes = date_object.minute
    return jsonify({'minutes': minutes})

@app.route('/commits/')
def commits_per_minute():
    response = requests.get('https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits')
    data = response.json()

    commits_per_minute = {}

    for commit in data:
        commit_date = commit['commit']['author']['date']
        minute = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ').minute
        if minute in commits_per_minute:
            commits_per_minute[minute] += 1
        else:
            commits_per_minute[minute] = 1

    minutes = list(commits_per_minute.keys())
    commit_counts = list(commits_per_minute.values())

    # Vous devrez utiliser ces données pour créer votre graphique

    return render_template('commits.html')

@app.route('/')
def hello_world():
    return render_template('hello.html') #comment2


if __name__ == "__main__":
    app.run(debug=True)
                                                                                                                                       
