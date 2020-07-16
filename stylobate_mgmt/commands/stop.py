import os

from .utils import docker, execute, Command

class Stop(Command):
    '''
    stylo stop --back-end/-b
               --front-end/-f
               --docker-dev/-d
               --docker-prod/-D
    '''

    name = 'stop'
    description = "Stops a currently running background process"
    
    def add_args(self, parser):
        parser.add_argument(
            '--docker-dev', '-d',
            action='store_true',
            help='Stops the dev docker container'
        )
        parser.add_argument(
            '--docker-prod', '-D',
            action='store_true',
            help='Stops the production docker container'
        )

    def main(self, args, basedir):
        if not (args.docker_dev or args.docker_prod or args.front_end):
            print('One of --docker-dev or --docker-prod must be specified')

        execute(docker.stop_command(docker.container_name(is_dev=args.docker_dev)))


