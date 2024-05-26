import sys
import subprocess
import os

commands_dir = 'Commands'
commands = {}

for subdir, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.realpath(__file__)), commands_dir)):
   for file in files:
      if file[0] == '_' :
        commands[(file.split('.')[0])[1:]] = file; 
         
n = len(sys.argv)

if n < 2:
    print("requires a command to be run")

if not commands.__contains__(sys.argv[0]):
    print(f"commands available: \n{commands}")
    sys.exit(1)

subprocess.call(sys.argv)





