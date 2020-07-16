from .utils import execute, Command

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
            help='Path to the directory that the project will be placed in')

    def main(self, args, basedir):
        print('Initializing new project {} in directory {}'.format(args.name, args.directory))
