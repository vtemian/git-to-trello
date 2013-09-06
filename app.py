from flask import Flask, render_template
from hook import hook
from github import github

app = Flask(__name__)

app.debug = True

app.register_blueprint(hook)
app.register_blueprint(github)

@app.route('/new')
def hello():
   return render_template('new.html')

if __name__ == '__main__':
  app.run()
