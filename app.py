from flask import Flask, render_template

from hook import hook
from github import github
from status import status
from tracker import tracker

app = Flask(__name__)

app.debug = True

app.register_blueprint(hook)
app.register_blueprint(github)
app.register_blueprint(status)
app.register_blueprint(tracker)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
  app.run()
