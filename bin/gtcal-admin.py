
import os
import sys
sys.path.append("..")
import gtcal
import argparse


DESCRIPTION = "A simple calendar app on the command line"
VERSION = "1.0.0"
EPILOG = "No bugs please"

def main(*argv):
    parser = argparse.ArgumentParser(description=DESCRIPTION, version=VERSION, epilog=EPILOG)

    parser.add_argument('csv', nargs = 1, help="Data to import")

    args = parser.parse_args()
    print args
if __name__ == "__main__":
    main(*sys.argv[1:])