import os

from .utils import docker, execute, Command

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
            '--silent', '-s',
            action='store_true',
            help='Run silently in background instead of tailing the logs'
        )

        parser.add_argument(
            '--user', '-u',
            metavar='username',
            nargs=1,
            help='Specify the username with which the docker image was named'
        )


    def main(self, args, basedir):
        if not (args.docker_dev or args.docker_prod or args.front_end or args.back_end):
            print('At least one of --docker-dev, --docker-prod, --back-end, or --front-end must be specified')
        if args.back_end:
            execute('venv/bin/uvicorn main:app --reload', wd=os.path.join(basedir, 'backend'))
        if args.front_end:
            execute('yarn start', wd=os.path.join(basedir, 'frontend'))

        docker_prefix = args.user[0] + '/' if args.user else ''

        if args.docker_dev:
            execute(docker.run_command(args.user, is_dev=True), wd=basedir)

        if args.docker_prod:
            execute(docker.run_command(args.user, is_dev=False), wd=basedir)



