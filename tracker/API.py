from trello import TrelloApi
import re

class TrackerAPI(object):

  def __init__(self, access_key, token):
    self.tracker = TrelloApi(access_key, token)

  def change_state(self, card, state):
    card_pattern = 'https://trello.com/c/(\w+)'

    try:
      card = re.search(card_pattern, card).group(1)
    except:
      return 'Invalid shortlink'

    self.clean_card(card)

    response = self.tracker.cards.new_label(card, state)
    return  response

  def clean_card(self, card):
    possible_state = ['green', 'red', 'yellow']

    for state in possible_state:
      try:
        self.tracker.cards.delete_label_color(state, card)
      except:
        pass
