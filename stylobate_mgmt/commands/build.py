import os

from .utils import docker, execute, Command

class Build(Command):
    '''
    stylo build --docker-dev/-d
            --docker-prod/-D
            --front-end/-f
            --user/-u <username>
    '''

    name = 'build'
    description = "Initializes a new Stylobate project, forking the original"
    
    def add_args(self, parser):
        parser.add_argument(
            '--docker-dev', '-d',
            action='store_true',
            help='Build the dev docker image'
        )
        parser.add_argument(
            '--docker-prod', '-D',
            action='store_true',
            help='Build the production docker image'
        )
        parser.add_argument(
            '--front-end', '-f',
            action='store_true',
            help='Build the front-end static files'
        )

        parser.add_argument(
            '--flow', '-F',
            action='store_true',
            help='Build the front-end static files, verifying Flow types'
        )

        parser.add_argument(
            '--user', '-u',
            metavar='username',
            nargs=1,
            help='Specify the username with which to name the docker image'
        )

    def main(self, args, basedir):
        if not (args.docker_dev or args.docker_prod or args.front_end or args.flow):
            print('At least one of --docker-dev, --docker-prod, or --front-end must be specified')

        if args.docker_dev:
            execute(docker.build_command(args.user, is_dev=True), wd=basedir)
        if args.docker_prod:
            execute('pip freeze > requirements.txt', wd=[basedir, 'backend'])
            execute(docker.build_command(args.user, is_dev=False), wd=basedir)
        if args.front_end:
            execute('yarn build', wd=[basedir, 'frontend'])
        if args.flow:
            execute('yarn flow', wd=[basedir, 'frontend'])


