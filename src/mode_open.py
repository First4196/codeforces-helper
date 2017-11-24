import subprocess

from exception import InvalidCommandError, InvalidContestNumError, InvalidProbNameError

def run(arg):

    if len(arg) >= 3:
        raise InvalidCommandError

    cf_url = 'http://codeforces.com/'

    if len(arg) == 0:
        openurl(cf_url+'contests')

    if len(arg) == 1:
        InvalidContestNumError.check(arg[0])
        contest_num = arg[0]
        openurl(cf_url+'contest/'+contest_num)

    if len(arg) == 2:
        InvalidContestNumError.check(arg[0])
        contest_num = arg[0]
        prob_name = arg[1]
        if prob_name == 'all':
            openurl(cf_url+'contest/'+contest_num+'/problems')
        else:
            InvalidProbNameError.check(prob_name)
            openurl(cf_url+'contest/'+contest_num+'/problem/'+prob_name)


def openurl(url):
    subprocess.run(['google-chrome',url])