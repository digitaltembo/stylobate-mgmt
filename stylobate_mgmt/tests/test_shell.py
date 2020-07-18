from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class ShellTest(CommandTest):
    command = 'shell'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'-dc', NAME: 'dev_certbot'},
    #         {CMD:'-dn', NAME: 'dev_nginx'},
    #         {CMD:'-db', NAME: 'dev_backend'},
    #         {CMD:'-df', NAME: 'dev_frontend'}, 

    #         {CMD:'-Dc', NAME: 'prod_certbot'},
    #         {CMD:'-Dn', NAME: 'prod_nginx'},
    #         {CMD:'-Db', NAME: 'prod_backend'},
    #         {CMD:'-Df', NAME: 'prod_frontend'}, 

    #         {CMD:'-sc', NAME: 'ssl_certbot'},
    #         {CMD:'-sn', NAME: 'ssl_nginx'},
    #         {CMD:'-sb', NAME: 'ssl_backend'},
    #         {CMD:'-sf', NAME: 'ssl_frontend'}, 
    #     ])

    def test_dev_certbot(self):
        self.assert_command({
            CMD: '-dc',
            EXPECTATION: [
                'There is no certbot container running'
            ]
        })

    def test_dev_nginx(self):
        self.assert_command({
            CMD: '-dn',
            EXPECTATION: [
                'There is no nginx container running'
            ]
        })

    def test_dev_backend(self):
        self.assert_command({
            CMD: '-db',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._backend_1 /bin/sh'
            ]
        })

    def test_dev_frontend(self):
        self.assert_command({
            CMD: '-df',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._frontend_1 /bin/sh'
            ]
        })

    def test_prod_certbot(self):
        self.assert_command({
            CMD: '-Dc',
            EXPECTATION: [
                'There is no certbot container running'
            ]
        })

    def test_prod_nginx(self):
        self.assert_command({
            CMD: '-Dn',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._nginx_prod_1 /bin/sh'
            ]
        })

    def test_prod_backend(self):
        self.assert_command({
            CMD: '-Db',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._backend_prod_1 /bin/sh'
            ]
        })

    def test_prod_frontend(self):
        self.assert_command({
            CMD: '-Df',
            EXPECTATION: [
                'There is no frontend container running'
            ]
        })

    def test_ssl_certbot(self):
        self.assert_command({
            CMD: '-sc',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._certbot_ssl_1 /bin/sh'
            ]
        })

    def test_ssl_nginx(self):
        self.assert_command({
            CMD: '-sn',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._nginx_ssl_1 /bin/sh'
            ]
        })

    def test_ssl_backend(self):
        self.assert_command({
            CMD: '-sb',
            EXPECTATION: [
                'cd .',
                'docker exec -it ._backend_ssl_1 /bin/sh'
            ]
        })

    def test_ssl_frontend(self):
        self.assert_command({
            CMD: '-sf',
            EXPECTATION: [
                'There is no frontend container running'
            ]
        })