import json

from flask import Blueprint, render_template, request
import requests

import config

auth = Blueprint('github', __name__, 'templates')

@auth.route('/github/auth', methods=['POST', 'GET'])
def get_token():
  data = {
    'scopes': [
      'repo',
    ],
    'client_id': config.CLIENT_ID,
    'client_secret': config.CLIENT_SECRET,
  }

  url = "https://api.github.com/authorizations"
  auth = (config.GITHUB_USER, config.GITHUB_PASSWORD)

  response = requests.post(url, data=json.dumps(data), auth=auth)
  response = json.loads(response.content)

  if 'token' in response:
    token = repsone['token']
    return render_template('auth.html', token=token)
  else:
    return render_template('response.html', response=str(json.dumps(response)))
