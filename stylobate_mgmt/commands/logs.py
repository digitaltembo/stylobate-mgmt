import os

from .utils import docker, execute, Command

class Logs(Command):
    '''
    stylo logs --docker-dev/-d
               --docker-prod/-D
               --less/-l
               --tail/-t
               --cat/-c
    '''

    name = 'logs'
    description = "Tails, cats or lesses the logs"
    
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
            '--less', '-l',
            action='store_true',
            help='Displays logs within less'
        )

        parser.add_argument(
            '--tail', '-t',
            action='store_true',
            help='Tails the logs'
        )

        parser.add_argument(
            '--cat', '-c',
            action='store_true',
            help='Cats the logs'
        )

    def main(self, args, basedir):
        if not (args.docker_dev or args.docker_prod):
            print('At least one of --docker-dev or --docker-prod must be specified')


        style = 'tail'
        if args.less:
            style = 'less'
        elif args.cat:
            style = 'cat'

        execute(docker.logs_command(docker.container_name(is_dev=args.docker_dev), style))


