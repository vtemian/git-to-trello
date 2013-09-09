from flask import Flask, render_template

from github.hook import hook
from github.auth import auth
from github.status import status

from tracker.trello_tracker import tracker

app = Flask(__name__)

app.debug = True

app.register_blueprint(hook)
app.register_blueprint(auth)
app.register_blueprint(status)
app.register_blueprint(tracker)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
  app.run()
