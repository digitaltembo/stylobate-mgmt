import os

from .utils import Command
SUPERUSER_INSERTION_FORMAT = '$(venv/bin/python -c "from db.models import User; User.create_superuser(\'{}\', \'{}\')")'
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

        parser.add_argument(
            '--execute', '-x',
            metavar='SQL_CMD',
            nargs=1,
            help='Run a SQL commadn (remember your semicolon!)'
        )

    def main(self, args):
        if not (args.up or args.up_one or args.down or args.shell or args.execute or args.gen_migrations):
            self.print('At least one of --up, --up-one, --down, --shell, or --gen-migrations must be specified')
            return
        if args.up:
            self.upgrade_all()
        elif args.up_one:
            self.upgrade_once()
        if args.down:
            self.downgrade()
        if args.gen_migrations:
            self.gen_migrations('' if args.gen_migrations == True else args.gen_migrations)
        if args.shell:
            self.enter_shell()
        if args.execute:
            self.execute_sql(args.execute[0])

    def upgrade_all(self):
        self.execute('venv/bin/alembic upgrade head', 'backend')

    def upgrade_once(self):
        self.execute('venv/bin/alembic upgrade +1', 'backend')

    def downgrade(self):
        self.execute('venv/bin/alembic downgrade -1', 'backend')

    def gen_migrations(self, message=''):
        message = ' -m "{}"'.format(message)
        self.execute('venv/bin/alembic revision --autogenerate' + message, 'backend')

    def enter_shell(self):
        self.execute('sqlite3 the.db', 'backend')

    def execute_sql(self, sql):
        self.execute('sqlite3 the.db "{}"'.format(sql), 'backend')

    def add_superuser(self, email, password):
        self.execute_sql(SUPERUSER_INSERTION_FORMAT.format(email, password))

