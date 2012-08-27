#!/usr/local/bin/python
import sys, re, os

def main():
    line()
    if len(sys.argv) >1:
        print "first argument is: %s" % sys.argv[1]
    else:
        print "no agument was supplied"
    line()


def line():
    print "="*40

if __name__ == '__main__':
    main()