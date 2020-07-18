from getpass import getpass
import os

from .utils import Command
from .db import DB

class Init(Command):
    name = 'init'
    description = "Initializes a new Stylobate project, forking the original"
    
    def add_args(self, parser):
        parser.add_argument(
            'name',
            type=str,
            help='The name of the stylobate project'
        )
        parser.add_argument(
            'directory',
            type=str,
            nargs='?',
            help='Path to the directory that the project will be placed in'
        )

    def main(self, args):
        parent_dir = args.directory if args.directory else os.getcwd()
        name = args.name
        self.initialize_project(args.name, parent_dir)

    def initialize_project(self, project_name, parent_dir):
        self.print('Initializing new project {} in directory {}'.format(project_name, parent_dir))

        self.execute('gh repo create -d "Stylobate-based Web Application" {}'.format(project_name), abs_dir=parent_dir)


        proj_dir = os.path.join(parent_dir, project_name)
        proj_ctxt = self.context.new_context(proj_dir)


        if not os.path.isdir(proj_dir):
            # So they shouuuld say yes while creating the repo to make this git directory locally, but they may not
            proj_ctxt.execute('mkdir {}'.format(project_name))
            proj_ctxt.execute('git init')
        else:
            # GitHub CLI clones the remote repo over HTTP :(
            proj_ctxt.execute('git remote remove origin')

        username = self.input("Username for 'https://github.com'")

        proj_ctxt.execute('git remote add origin git@github.com:{}/{}.git'.format(username, project_name))
        proj_ctxt.execute('git remote add upstream git@github.com:digitaltembo/stylobate.git')
        proj_ctxt.execute('git pull upstream master')
        proj_ctxt.execute('git push -u origin master')

        proj_ctxt.execute('python -m venv venv', 'backend')
        proj_ctxt.execute('venv/bin/pip install -r requirements.txt', 'backend')

        proj_ctxt.execute('yarn install', 'frontend')

        username = self.input("Superuser email")
        password = self.input("Superuser password")

        DB(proj_ctxt).add_superuser(username, password)





