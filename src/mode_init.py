import os
import shutil

from exception import InvalidCommandError, InvalidContestNameError, InvalidNumProbError, ContestFolderAlreadyExistError

def run(arg):

    if len(arg) == 0 or len(arg) >= 3:
        raise InvalidCommandError

    if len(arg) == 1:
        arg.append('5')

    if len(arg) == 2:

        # check contest name
        InvalidContestNameError.check(arg[0])
        contest_name = arg[0]

        # check num prob
        InvalidNumProbError.check(arg[1])
        num_prob = int(arg[1])

        # check folder already exist
        folder_path = os.environ['CF'] + '/' + contest_name
        ContestFolderAlreadyExistError.check(folder_path)

        # init contest
        os.makedirs(folder_path)
        os.chdir(folder_path)

        makefile_path = os.environ['CF_HELPER'] + '/res/Makefile'
        with open('Makefile', 'w') as new_makefile:
            first_line = 'all: ' + ' '.join([chr(ord('A') + i) for i in range(num_prob)])
            new_makefile.write(first_line)
            with open(makefile_path, 'r') as makefile:
                for line in makefile:
                    new_makefile.write(line)

        template_path = os.environ['CF_HELPER'] + '/res/template.cpp'
        for i in range(num_prob):
            shutil.copy(template_path, chr(ord('A') + i) + '.cpp')

        print('Initailized contest with', num_prob, 'problems.')
