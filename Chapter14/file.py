#!/usr/bin/python3
import sys
count = len(sys.argv)
name = ''

name = input("Enter a name: ") if ( count == 1 ) else sys.argv[1]
with open("/tmp/script.log","a") as log:
    log.write(f"Hello {name}" + "\n")
