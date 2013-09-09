from trello import TrelloApi

import config

class Tracker(object):

  def __init__(self):
    self.wrapper = TrelloApi(config.TRELLO_KEY, config.TRELLO_TOKEN)

  def change_state(self, card, state):
    try:
      print self.wrapper.cards.delete_label_color('green', card)
    except:
      pass
    print self.wrapper.cards.new_label(card, 'red')

if __name__ == '__main__':
  tracker = Tracker()
  tracker.change_state('VXViQZQl', 'asd')
