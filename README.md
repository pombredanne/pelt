# pelt - Python ELectron Terminal
## About
The goal of pelt is to experiment with various technologies to create a small, flexible, and customizable terminal emulator.

Currently pelt is written primarily in Python for the heavy lifting, with JavaScript, HTML, and CSS handled by Flask to be used for the user interface implemented with Electron.
## Running
You can run pelt using `electron` ([Electron](http://electron.atom.io/)). You need to first go to the root directory of pelt (where package.json is), and make sure to do the following:
```
# Make sure to install node.js dependencies
npm install

# Make sure you have Python installed
python --version
```
Once you've done this you can run pelt normally:
```
# Using globally installed electron
electron .
```
You can also run pelt without the GUI and use a browser (not recommended):
```
# You can access the page at http://localhost:5000/
python src/main.py
```
