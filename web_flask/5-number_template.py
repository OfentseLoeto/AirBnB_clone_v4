#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """Display 'hbnb!'"""
    return 'hbnb'

@app.route('/c/<text>' ,strict_slashes=False)

def c_text(text):
    """display “C ”, followed by the value of the text variable
       (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/(<text>)', strict_slashes=False)

def python_text(text):
    """display “Python ”, followed by the value of the text variable
       (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<n>', strict_slashes=False)

def number(n):
    """display “n is a number” only if n is an integer"""
    return '{} is an integer'.format(n)

@app.route('/number_template<n>', strict_slashes=False)

def number_template(n):
    """Display an HTML page with an H1 tag containing 'Number: n' inside the BODY"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
