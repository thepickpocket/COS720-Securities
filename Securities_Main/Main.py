# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print('The main function, where we should call stuff from.')

if __name__ == "Main":
    main() #This is where the main function will be called.


class Main:
    # Constructor for Python
    def __init__(self):
        print 'Hello World! ', 'This is me.\n';