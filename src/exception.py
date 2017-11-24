import os
import re

class CustomException(Exception):
    def __str__(self):
        return "custom exception"
    @classmethod
    def check(cls,arg):
        if False:
            raise cls

class ContestFolderAlreadyExistError(CustomException):
    def __str__(self):
        return "contest folder already exists"
    @classmethod
    def check(cls,arg):
        if os.path.exists(arg):
            raise cls

class ContestFolderNotExistError(CustomException):
    def __str__(self):
        return "contest folder not exists"
    @classmethod
    def check(cls,arg):
        if not os.path.exists(arg):
            raise cls
        

class InvalidCommandError(CustomException):
    def __str__(self):
        return "invalid command\n" +\
                "try using 'cf help'"
    @classmethod
    def check(cls,arg):
        if False:
            raise cls

class InvalidContestNameError(CustomException):
    def __str__(self):
        return "invalid contest name\n" +\
                "only alphanumerics and underscores are allowed"
    @classmethod
    def check(cls,arg):
        if not re.match(r'^\w+$', arg):
            raise cls

class InvalidContestNumError(CustomException):
    def __str__(self):
        return "invalid contest number\n" +\
                "contest number should be positive integers"
    @classmethod
    def check(cls,arg):
        if not re.match(r'^\d+$', arg):
            raise cls

class InvalidProbNameError(CustomException):
    def __str__(self):
        return "invalid problem name\n" +\
                "problem name should be single english alphabet"
    @classmethod
    def check(cls,arg):
        if not re.match(r'^[a-zA-Z]$', arg):
            raise cls

class InvalidNumProbError(CustomException):
    def __str__(self):
        return "invalid number of problems\n" +\
                "number of problems should be number between 1 to 26"
    @classmethod
    def check(cls,arg):
        try:
            n = int(arg)
        except ValueError:
            raise cls
        if not ( 1 <= n <= 26 ):
            raise cls
