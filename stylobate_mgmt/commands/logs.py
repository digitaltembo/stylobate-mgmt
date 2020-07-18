import os

from .utils import docker, Command

TAIL = 'docker-compose -f {} logs -f'
LESS = 'docker-compose -f {} logs | less'
CAT  = 'docker-compose -f {} logs'

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
            help='Display logs from the dev docker image'
        )
        parser.add_argument(
            '--docker-prod', '-D',
            action='store_true',
            help='Display logs from the production docker image'
        )
        parser.add_argument(
            '--docker-ssl', '-s',
            action='store_true',
            help='Display logs from the production docker image with SSL'
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

    def main(self, args):
        if not (args.docker_dev or args.docker_prod or args.docker_ssl):
            self.print('At least one of --docker-dev, --docker-prod, --docker-ssl, must be specified')
            return

        style = TAIL
        if args.less:
            style = LESS
        elif args.cat:
            style = CAT
        docker_env = docker.get_env(args)
        self.display_docker_logs(docker_env, style)

    def display_docker_logs(self, docker_env, style):
        self.execute(style.format(docker_env))


