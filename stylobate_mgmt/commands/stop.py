import os

from .utils import docker, Command

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
        parser.add_argument(
            '--docker-ssl', '-s',
            action='store_true',
            help='Stops the ssl docker container'
        )

    def main(self, args):
        if not (args.docker_dev or args.docker_prod or args.docker_ssl):
            self.print('One of --docker-dev, --docker-prod, or --docker-ssl must be specified')
            return
        docker_env = docker.get_env(args)

        self.stop_docker(docker_env)
    
    def stop_docker(self, docker_env):
        self.execute('docker-compose -f {} down'.format(docker_env))


