"""pelt class for terminal commands.
"""

class Command(object):
    """Command class.

    Associates a string with a function to form a terminal command.
    """
    def __init__(self, name="", func=None):
        self.name = name
        self.func = func

# Command class tests
if __name__ == "__main__":
    def test():
        """Function for Command class test."""
        print "Hello world!"
    tvar = Command(name="test", func=test)
    print tvar.name
    tvar.func()
