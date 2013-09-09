import json

from flask import Blueprint, render_template, request
import requests

import config

status = Blueprint('status', __name__, 'templates')

@status.route('/status')
def index():
  return render_template('status.html')

@status.route('/status/new', methods=['POST'])
def new():
  data = {
    "state": request.form['state'],
    "description": request.form['description'],
  }

  sha = request.form['sha']
  user = request.form['user']
  repo = request.form['repo']
  auth_url = "?access_token=%s" % config.GITHUB_TOKEN

  url = "https://api.github.com/repos/%s/%s/statuses/%s%s" % (user, repo, sha, auth_url)

  response = requests.post(url, data=json.dumps(data))

  return render_template('response.html', response=response.content)
