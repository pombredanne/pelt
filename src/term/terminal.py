"""pelt underlying terminal.
"""

from commands import __commands__
from Queue import Queue

LOG_MAX = 256

def check_command(command):
    """Checks if given command is valid"""
    for cmd in __commands__:
        if command == cmd.name:
            return True
    return False

def exec_cmd(argc=0, argv=None):
    """Manages command execution for the terminal."""
    if argc == 0:
        return term_help()
    elif check_command(argv[0]):
        return
    else:
        return term_help()

def term_help():
    """Generates term_help info for the terminal."""
    ret_str = "<ul>"
    for cmd in __commands__:
        ret_str += "<li>"
        ret_str += cmd.name
        ret_str += "</li>"
    ret_str += "</ul>"
    return ret_str

class Terminal(object):
    """Terminal class."""
    def __init__(self, name="", size=0):
        self.name = name
        if size > 0:
            self.log = Queue(size)
        else:
            self.log = Queue(LOG_MAX)

    def write_line(self, line=""):
        """Writes line to the terminal log"""
        print line
        if self.log.full():
            self.log.get_nowait()
            self.log.put(line)
        else:
            self.log.put(line)
        return None

    def parse_str(self, in_str=""):
        """Converts raw string input for use in exec_cmd()"""
        self.write_line(in_str)
        return None
