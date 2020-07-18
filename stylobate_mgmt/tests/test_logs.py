from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class LogsTest(CommandTest):
    command = 'logs'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'-dt', NAME: 'dev_tail'},
    #         {CMD:'-dl', NAME: 'dev_less'},
    #         {CMD:'-dc', NAME: 'dev_cat'},
    #         {CMD:'-Dt', NAME: 'prod_tail'},
    #         {CMD:'-Dl', NAME: 'prod_less'},
    #         {CMD:'-Dc', NAME: 'prod_cat'},
    #         {CMD:'-st', NAME: 'ssl_tail'},
    #         {CMD:'-sl', NAME: 'ssl_less'},
    #         {CMD:'-sc', NAME: 'ssl_cat'},
    #         {CMD: '-t', NAME: 'no_docker_env'}
    #     ])
    
    def test_dev_tail(self):
        self.assert_command({
            CMD: '-dt',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml logs -f'
            ]
        })

    def test_dev_less(self):
        self.assert_command({
            CMD: '-dl',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml logs | less'
            ]
        })

    def test_dev_cat(self):
        self.assert_command({
            CMD: '-dc',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml logs'
            ]
        })

    def test_prod_tail(self):
        self.assert_command({
            CMD: '-Dt',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml logs -f'
            ]
        })

    def test_prod_less(self):
        self.assert_command({
            CMD: '-Dl',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml logs | less'
            ]
        })

    def test_prod_cat(self):
        self.assert_command({
            CMD: '-Dc',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml logs'
            ]
        })

    def test_ssl_tail(self):
        self.assert_command({
            CMD: '-st',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml logs -f'
            ]
        })

    def test_ssl_less(self):
        self.assert_command({
            CMD: '-sl',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml logs | less'
            ]
        })

    def test_ssl_cat(self):
        self.assert_command({
            CMD: '-sc',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml logs'
            ]
        })

    def test_no_docker_env(self):
        self.assert_command({
            CMD: '-t',
            EXPECTATION: [
                'At least one of --docker-dev, --docker-prod, --docker-ssl, must be specified'
            ]
        })
