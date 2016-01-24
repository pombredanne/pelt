"""pelt terminal commands.
"""

from command import Command

# ls - lists files in current directory
def ls_func():
    # Do something here
    return
LS = Command(name="ls", func=ls_func)

# Array of commands
__commands__ = [LS]
