import os

from .utils import docker, Command

class Shell(Command):
    '''
    style shell --docker-dev/-d
                --docker-prod/-D
    '''

    name = 'shell'
    description = "Enters into the docker shell of a currently running container. Need to choose the docker environment and the specific container"
    
    def add_args(self, parser):
        parser.add_argument(
            '--docker-dev', '-d',
            action='store_true',
            help='Access the shell of the development docker image'
        )
        parser.add_argument(
            '--docker-prod', '-D',
            action='store_true',
            help='Access the shell of the production docker image'
        )
        parser.add_argument(
            '--docker-ssl', '-s',
            action='store_true',
            help='Access the shell of the production docker image with SSL'
        )

        parser.add_argument(
            '--certbot', '-c',
            action='store_true',
            help='Access the certbot shell'
        )
        parser.add_argument(
            '--nginx', '-n',
            action='store_true',
            help='Access the nginx shell'
        )
        parser.add_argument(
            '--back-end', '-b',
            action='store_true',
            help='Access the backend shell'
        )
        parser.add_argument(
            '--front-end', '-f',
            action='store_true',
            help='Access the frontend shell'
        )

    def main(self, args):
        if not (args.docker_dev or args.docker_prod or args.docker_ssl):
            self.print('One of --docker-dev, --docker-prod, or --docker-ssl must be specified')
            return
        if not (args.certbot or args.nginx or args.back_end or args.front_end):
            self.print('One of --certbot, --nginx, --backend, or --frontend must be specified')
            return

        docker_env = docker.get_env(args)
        docker_image = docker.get_img(args)
        self.enter_shell(docker_env, docker_image)
    def enter_shell(self, docker_env, docker_image):
        if not docker.env_has_container(docker_env, docker_image):
            self.print('There is no {} container running'.format(docker_image))
            return
        container = docker.container_name(self.context.project_name, docker_env, docker_image)

        self.execute('docker exec -it {} /bin/sh'.format(container))

