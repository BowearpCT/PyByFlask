
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author' : 'Chaiyasit',
        'title' : 'My love',
        'content' : 'First post content',
        'date' : 'April 20, 2018'
    },
    {
        'author' : 'Bow',
        'title' : 'My Bad',
        'content' : 'second',
        'date' : 'April 20, 2019'
    }

]


@app.route('/home')
def Home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return ""


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000)