# -*- coding: utf-8 -*-
"""pelt main python file.

Handles communication between Electron/Flask and the terminal code.
"""
from flask import Flask, render_template, request, send_from_directory
from term import Terminal
from theme import Theme
import os

# Global variables
THEMES = list()
TERMINAL = Terminal(name='main')

# Load themes
THEMES_DIR = os.getcwd() + '/themes/'
for root in os.walk(THEMES_DIR):
    for folder in root[1]:
        THEMES.append(Theme(path=THEMES_DIR+folder))

# Initialize flask app
if len(THEMES) > 0:
    APP = Flask(__name__, static_folder=THEMES_DIR + THEMES[0].name)
else:
    APP = Flask(__name__)
APP.debug = False

@APP.route('/')
def peyl_page():
    """Provides the main.html template"""
    return render_template('main.html')

@APP.route('/', methods=['POST'])
def handle_input():
    """Sends input from pelt page into pelt terminal"""
    _input = request.form['text']
    TERMINAL.parse_str(_input)
    return render_template('main.html', log=list(TERMINAL.log.queue))

@APP.route('/main.js')
def main_js():
    """Provides the main.js file for the main.html page"""
    return send_from_directory(os.getcwd() + '/src', 'main.js')

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port='5000')
