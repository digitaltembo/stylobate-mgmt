import sys
import argparse
import os

from .commands.utils import CommandContext

from .commands import *

"""
Tool for managing stylobate projects

Example commands
stylo init
stylo build --docker-dev/-d
            --docker-prod/-D
            --front-end/-f
stylo run --back-end/-b
          --front-end/-f
          --docker-dev/-d
          --docker-prod/-D
          --logs

stylo logs --docker-dev/-d
           --docker-prod/-D

style shell --docker-dev/-d
            --docker-prod/-D

stylo stop --back-end/-b
           --front-end/-f
           --docker-dev/-d
           --docker-prod/-D

stylo db --up/-u
         --down/-d
         --gen-migrations/-g
"""

COMMAND_MAP = {
    'db': DB,
    'build': Build,
    'init': Init,
    'logs': Logs,
    'run': Run,
    'shell': Shell,
    'stop': Stop
}

def main():
    args = sys.argv 

    if len(args) == 1:
        help()
    command = args[1]

    if command in ['-h', '--help', 'help']:
        help()

    base = basedir()


    if command not in COMMAND_MAP:
        print('stylo command must be one of init, build, run, logs, shell, stop, or db')
        return

    if command != 'init' and not base:
        print('This must be executed from within a Stylobate project directory')
        return
    
    run(command, CommandContext(base), args[2:])

def run(command, commandContext, args):
    COMMAND_MAP[command](commandContext).run(args)

def help():
    print('''
usage: stylo [--help] <command> [<args>]

 ,---.   ,--.           ,--.       ,--.             ,--.          
'   .-',-'  '-.,--. ,--.|  | ,---. |  |-.  ,--,--.,-'  '-. ,---.  
`.  `-.'-.  .-' \  '  / |  || .-. || .-. '' ,-.  |'-.  .-'| .-. : 
.-'    | |  |    \   '  |  |' '-' '| `-' |\ '-'  |  |  |  \   --. 
`-----'  `--'  .-'  /   `--' `---'  `---'  `--`--'  `--'   `----' 
               `---'                                              
_________________________________________________________________

Manage https://github.com/digitaltembo/stylobate based projects!

These are the stylo commands one can use:

init  - Initialize a new stylobate project
build - Build project for specific deployment
run   - Run project
logs  - Display logs for project
shell - Access shell within running project
stop  - Terminate server
db    - Manage database

Run stylo <command> --help/-h for help on a particular command
    ''')
    exit()

def basedir():
    cwd = os.getcwd()
    dirs = cwd.split('/')
    # iterate up the file tree
    def has_child_dir(dir, child_dir):
        return os.path.isdir(os.path.join(dir, child_dir)) 

    for i in range(len(dirs), 1, -1):
        iter_dir = '/'.join(dirs[:i])
        if has_child_dir(iter_dir, 'frontend') and has_child_dir(iter_dir, 'backend'):
            return iter_dir 

    return None

if __name__ == '__main__':
    main()