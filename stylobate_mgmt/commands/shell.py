import os

from .utils import docker, execute, Command

class Shell(Command):
    '''
    style shell --docker-dev/-d
                --docker-prod/-D
    '''

    name = 'shell'
    description = "Enters into the docker shell of a currently running container"
    
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

    def main(self, args, basedir):
        if not (args.docker_dev or args.docker_prod):
            print('One of --docker-dev or --docker-prod must be specified')
        execute(docker.shell_command(docker.container_name(is_dev=args.docker_dev)))

