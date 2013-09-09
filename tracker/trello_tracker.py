import json
import re

from trello import TrelloApi
from flask import Blueprint, render_template, request
import requests

import config

tracker = Blueprint('tracker', __name__, 'templates')

@tracker.route('/tracker/change_label', methods=['GET'])
def trello():
  return render_template('change_label.html')

@tracker.route('/tracker/change_label', methods=['POST'])
def change_label():
  wrapper = TrelloApi(config.TRELLO_KEY, config.TRELLO_TOKEN)

  card_pattern = 'https://trello.com/c/(\w+)'

  try:
    card = re.search(card_pattern, request.form['card']).group(1)
  except:
    return render_template('response.html', response='Invalid shortlink')

  try:
    wrapper.cards.delete_label_color(request.form['state'], card)
  except:
    pass

  response = wrapper.cards.new_label(card, request.form['state'])

  return render_template('response.html', response=response)
