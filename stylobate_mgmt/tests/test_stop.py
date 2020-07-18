from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class StopTest(CommandTest):
    command = 'stop'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'-d', NAME: 'docker_dev'},
    #         {CMD:'-D', NAME: 'docker_prod'},
    #         {CMD:'-s', NAME: 'docker_ssl'},
    #     ])

    def test_docker_dev(self):
        self.assert_command({
            CMD: '-d',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml down'
            ]
        })

    def test_docker_prod(self):
        self.assert_command({
            CMD: '-D',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml down'
            ]
        })

    def test_docker_ssl(self):
        self.assert_command({
            CMD: '-s',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml down'
            ]
        })