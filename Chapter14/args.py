#!/usr/bin/python3
import sys
count = len(sys.argv)
name = ''

name = input("Enter a name: ") if ( count == 1 ) else sys.argv[1]
print(f"Hello {name}")
print(f"Exiting {sys.argv[0]}")
