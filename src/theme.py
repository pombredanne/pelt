"""pelt theme module.
"""

import json

class Theme(object):
    """pelt Theme class.
    """
    def __init__(self, path=""):
        self.json_path = path + '/style.json'
        json_data = json.load(open(self.json_path))
        self.name = json_data["name"]
        self.author = json_data["author"]
        self.css_path = self.name + '/style.css'
