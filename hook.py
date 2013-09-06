import json

from flask import Blueprint, render_template, request
import requests

import config

hook = Blueprint('hooks', __name__, 'templates')

@hook.route('/hook/new', methods=['POST'])
def new():
  data = {
    "name": request.form['name'],
    "active": request.form['active'] if 'active' in request.form else 'false',
    "events": request.form['events'].split(','),
    "config": {
      "url": request.form['url'],
      "content_type": request.form['content_type']
    }
  }

  auth_url = "?access_token=%s" % config.GITHUB_TOKEN
  url = "%s%s" % ("https://api.github.com/repos/vtemian/todopy/hooks", auth_url)

  response = requests.post(url, data=json.dumps(data))

  return render_template('response.html', response=response.content)