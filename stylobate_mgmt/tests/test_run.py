from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class RunTest(CommandTest):
    command = 'run'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'-b', NAME: 'backend'},
    #         {CMD:'-f', NAME: 'frontend'},
    #         {CMD:'-d', NAME: 'docker_dev'},
    #         {CMD:'-D', NAME: 'docker_prod'},
    #         {CMD:'-s', NAME: 'docker_ssl'},
    #         {CMD:'-dB', NAME: 'docker_dev_background'},
    #         {CMD:'-DB', NAME: 'docker_prod_background'},
    #         {CMD:'-sB', NAME: 'docker_ssl_background'}
    #     ])

    def test_backend(self):
        self.assert_command({
            CMD: '-b',
            EXPECTATION: [
                'cd ./backed',
                'venv/bin/uvicorn main:app --reload'
            ]
        })

    def test_frontend(self):
        self.assert_command({
            CMD: '-f',
            EXPECTATION: [
                'cd ./frontend',
                'yarn start'
            ]
        })

    def test_docker_dev(self):
        self.assert_command({
            CMD: '-d',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml up'
            ]
        })

    def test_docker_prod(self):
        self.assert_command({
            CMD: '-D',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml up'
            ]
        })

    def test_docker_ssl(self):
        self.assert_command({
            CMD: '-s',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml up'
            ]
        })

    def test_docker_dev_background(self):
        self.assert_command({
            CMD: '-dB',
            EXPECTATION: [
                'cd .',
                'docker-compose -f dev-compose.yaml up --detach'
            ]
        })

    def test_docker_prod_background(self):
        self.assert_command({
            CMD: '-DB',
            EXPECTATION: [
                'cd .',
                'docker-compose -f prod-compose.yaml up --detach'
            ]
        })

    def test_docker_ssl_background(self):
        self.assert_command({
            CMD: '-sB',
            EXPECTATION: [
                'cd .',
                'docker-compose -f ssl-compose.yaml up --detach'
            ]
        })