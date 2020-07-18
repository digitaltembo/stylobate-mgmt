import os
import fileinput

from .utils import docker, Command

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
            '--docker-ssl', '-s',
            action='store_true',
            help='Build the production docker image with SSL'
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

    def main(self, args):
        if not (args.docker_dev or args.docker_prod or args.docker_ssl or args.front_end or args.flow):
            self.print('At least one of --docker-dev, --docker-prod, --docker-ssl, or --front-end must be specified')
            return

        if args.front_end:
            self.frontend_build()
        elif args.flow:
            self.flow_build()
        else:
            docker_env = docker.get_env(args)
            self.docker_build(docker_env)

    def docker_build(self, docker_env):
        if docker_env == docker.PROD or docker_env == docker.SSL:
            self.frontend_build()
        if docker_env == docker.SSL:
            if not os.path.isfile(self.context.rel_path('certbot/conf/ssl-dhparams.pem')):
                self.init_certbot()

        self.execute('docker-compose -f {} build'.format(docker_env))

    def frontend_build(self):
        self.execute('yarn build', rel_dir='frontend')

    def flow_build(self):
        self.execute('yarn flow', rel_dir='frontend')

    def init_certbot(self):
        domain = self.input('What domain will this be hosted at? (ignoring subdomains)')
        subdomains = [s for s in self.input('What subdomains need this be valid for? ').split(' ') if s]

        domains = [domain] if len(subdomains) == 0 else [s + '.' for s in subdomains]

        email = self.input('What email should be attached to this certificate? ')
        if not self.confirm('This will initialize a LetsEncrypt certificate under the email {} at the domains {}. Is this correct? '.format(email, domains)):
            self.init_certbot()

        self.print('Editing nginx/ssl.conf')
        if not self.context.dry_run:
            # Edit nginx conf to use correct domain
            ssl_conf_file = self.context.rel_path('nginx/ssl.conf')
            ssl_conf_lines = []
            with open(ssl_conf_fil) as f:
                ssl_conf_lines = f.readlines()
            with open(ssl_conf_file, 'w') as f:
                for line in ssl:
                    f.write(line.replace('example.org', domain))

        # intialize certificates with init_letsencrypt script
        self.execute('certbot/init-letsencrypt "{}" {}'.format(domains, email))






