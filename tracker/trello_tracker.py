import json

from flask import Blueprint, render_template, request
import requests

import config
from tracker.API import TrackerAPI

tracker = Blueprint('tracker', __name__, 'templates')

@tracker.route('/tracker/change_label', methods=['GET'])
def trello():
  return render_template('change_label.html')

@tracker.route('/tracker/change_label', methods=['POST'])
def change_label():
  tracker = TrackerAPI(config.TRELLO_KEY, config.TRELLO_TOKEN)

  response = tracker.change_state(request.form['card'], request.form['state'])
  return render_template('response.html', response=response)
