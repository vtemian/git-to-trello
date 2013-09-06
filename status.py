import json

from flask import Blueprint, render_template, request
import requests

import config

status = Blueprint('statu', __name__, 'templates')

@status.route('/status/new', methods=['GET'])
def new():
  data = {
    "state": 'success',
    "description": 'test',
  }

  auth_url = "?access_token=%s" % config.GITHUB_TOKEN
  sha = 'bb1109d975fb0208525c78334a0a8d0a97c4319b'
  url = "%s%s" % ("https://api.github.com/repos/vtemian/todopy/statuses/"+sha, auth_url)

  response = requests.post(url, data=json.dumps(data))

  return render_template('response.html', response=response.content)


