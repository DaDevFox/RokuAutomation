import sys
import subprocess
import os
import commands

argv = sys.argv
if argv[0] == 'python':
    argv.pop(0)

n = len(argv)

if n < 3:
    print("requires a command to be run and a provided device IP address\n")
    sys.exit(1)


function = getattr(commands, argv[1])
if not function: 
    print(f"not a valid command\n")
    sys.exit(1)
else:
    function(*argv[2:])