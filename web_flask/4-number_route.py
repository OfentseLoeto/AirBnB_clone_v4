#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """Dispaly 'HBNB!'"""
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)

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
    python = text.replace('_', ' ')
    text = 'python {}'.format(text)

@app.route('/number/<n>', strict_slashes=False)

def number_n(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
