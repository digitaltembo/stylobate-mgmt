from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION

class BuildTest(CommandTest):
    command = 'build'

    def test_docker_dev(self):
        self.assert_command({
            CMD: '-d',
            EXPECTATION: ['cd .', 'docker-compose -f dev-compose.yaml build']
        })
    def test_docker_prod(self):
        self.assert_command({
            CMD: '-D',
            EXPECTATION: ['cd ./frontend', 'yarn build', 'cd .', 'docker-compose -f prod-compose.yaml build']
        })
    def test_docker_ssl(self):
        self.assert_command({
            CMD: '-s',
            INPUT: ['test.com',
                    'www',
                    'test@test.com',
                    'y'
            ],
            EXPECTATION: [
                'cd ./frontend',
                'yarn build',
                'Editing nginx/ssl.conf',
                'cd .',
                'certbot/init-letsencrypt "[\'www.\']" test@test.com',
                'cd .',
                'docker-compose -f ssl-compose.yaml build'
            ]
        })

    def test_frontend(self):
        self.assert_command({
            CMD: '-f',
            EXPECTATION: ['cd ./frontend', 'yarn build']
        })

    def test_flow(self):
        self.assert_command({
            CMD: '-F',
            EXPECTATION: ['cd ./frontend', 'yarn flow']
        })