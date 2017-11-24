import sys

import mode_help
import mode_init
import mode_fix
import mode_open

from exception import CustomException, InvalidCommandError

def main():
    arg = sys.argv[1:]
    n = len(arg)
    if n == 0:
        raise InvalidCommandError
    else:
        mode = arg[0]
        if mode == 'help':
            mode_help.run(arg[1:])
        elif mode == 'init':
            mode_init.run(arg[1:])
        elif mode == 'fix':
            mode_fix.run(arg[1:])
        elif mode == 'open':
            mode_open.run(arg[1:])
        else:
            raise InvalidCommandError

if __name__ == '__main__':
    try:
        main()
    except CustomException as errorMessage:
        print("Error:",errorMessage)
