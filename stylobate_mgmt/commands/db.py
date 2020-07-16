import os

from .utils import execute, Command

class DB(Command):
    '''
        stylo db --up/-u
                 --down/-d
                 --gen-migrations/-g
                 --shell/-s
    '''

    name = 'run'
    description = "Manages the DB of a Stylobate project, using Alembic"
    
    def add_args(self, parser):
        parser.add_argument(
            '--up', '-u',
            action='store_true',
            help='Runs all unrun migrations'
        )

        parser.add_argument(
            '--up-one', '-U',
            action='store_true',
            help='Runs the next unrun migrations'
        )

        parser.add_argument(
            '--down', '-d',
            action='store_true',
            help='Reverts last migration'
        )

        parser.add_argument(
            '--gen-migrations', '-g',
            metavar='message',
            const=True,
            nargs='?',
            help='Generates migrations from differences within the models folder, with an optional message'
        )

        parser.add_argument(
            '--shell', '-s',
            action='store_true',
            help='Enter DB CLI'
        )

    def main(self, args, basedir):
        if not (args.up or args.up_one or args.down or args.gen_migrations):
            print('At least one of --up, --up-one, --down, --shell, or --gen-migrations must be specified')

        wd = [basedir, 'backend']
        if args.up:
            execute('alembic upgrade head', wd)
        if args.up_one:
            execute('alembic upgrade +1', wd)
        if args.down:
            execute('alembic downgrade -1', wd)
        if args.gen_migrations:
            if args.gen_migrations == True:
                execute('alembic revision --autogenerate', wd)
            else:
                execute('alembic revision --autogenerate -m "{}"'.format(args.gen_migrations), wd)
        if args.shell:
            execute('sqlite3 the.db', wd)

