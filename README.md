# codeforces-helper
Tool for managing codes for codeforces contests wriiten in python

-------------
commands list
-------------

cf help
    -> get commands list

cf init <contest_name> <num_prob>
    -> create contest with specified name and number of problems
    -> <num_prob> will be assumned to be 5 if not specified

cf fix <contest_name> <num_prob>
    -> fix contest with specified name and number of problems
    -> <num_prob> will be assumned to be 5 if not specified

cf open
    -> open codeforces contests page in google chrome

cf open <contest_name> 
    -> open dashboard of specified contest in google chrome

cf open <contest_name> all
    -> open complete problemset of specified contest in google chrome

cf open <contest_name> <prob_name>
    -> open specified problem in specified contest in google chrome
