import os

from .utils import docker, Command

class Run(Command):
    '''
    stylo run --back-end/-b
              --front-end/-f
              --docker-dev/-d
              --docker-prod/-D
              --logs
    '''

    name = 'run'
    description = "Deploys a version of the stylobyte project"
    
    def add_args(self, parser):
        parser.add_argument(
            '--docker-dev', '-d',
            action='store_true',
            help='Run the dev docker image'
        )
        parser.add_argument(
            '--docker-prod', '-D',
            action='store_true',
            help='Run the production docker image'
        )
        parser.add_argument(
            '--docker-ssl', '-s',
            action='store_true',
            help='Run the production docker image with SSL'
        )

        parser.add_argument(
            '--front-end', '-f',
            action='store_true',
            help='Run the react-scripts front-end server'
        )

        parser.add_argument(
            '--back-end', '-b',
            action='store_true',
            help='Run the Uvicorn back-end server'
        )

        parser.add_argument(
            '--background', '-B',
            action='store_true',
            help='Run silently in background instead of tailing the logs'
        )


    def main(self, args):
        if not (args.docker_dev or args.docker_prod or args.docker_ssl or args.front_end or args.back_end):
            self.print('At least one of --docker-dev, --docker-prod, --back-end, or --front-end must be specified')
            return
        if args.back_end:
            self.serve_backend()
            return
        if args.front_end:
            self.serve_frontend()
            return
        if (args.docker_dev or args.docker_prod or args.docker_ssl):
            self.serve_docker(docker.get_env(args), args.background)

    def serve_backend(self):
        self.execute('venv/bin/uvicorn main:app --reload', 'backed')

    def serve_frontend(self):
        self.execute('yarn start', 'frontend')

    def serve_docker(self, docker_env, in_background):
        self.execute('docker-compose -f {} up{}'.format(docker_env, ' --detach' if in_background else ''))


