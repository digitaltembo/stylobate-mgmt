from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class DBTest(CommandTest):
    command = 'db'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'-u', NAME: 'up'},
    #         {CMD:'-U', NAME: 'up_all'},
    #         {CMD:'-d', NAME: 'downgrade'},
    #         {CMD:'-g', NAME: 'gen_migrations'},
    #         {CMD:'-s', NAME: 'shell'},
    #         {CMD:'-x', NAME: 'execute'},
    #     ])
    def test_up(self):
        self.assert_command({
            CMD: '-u',
            EXPECTATION: [
                'cd ./backend',
                'venv/bin/alembic upgrade head'
            ]
        })

    def test_up_all(self):
        self.assert_command({
            CMD: '-U',
            EXPECTATION: [
                'cd ./backend',
                'venv/bin/alembic upgrade +1'
            ]
        })

    def test_downgrade(self):
        self.assert_command({
            CMD: '-d',
            EXPECTATION: [
                'cd ./backend',
                'venv/bin/alembic downgrade -1'
            ]
        })

    def test_gen_migrations(self):
        self.assert_command({
            CMD: '-g',
            EXPECTATION: [
                'cd ./backend',
                'venv/bin/alembic revision --autogenerate -m ""'
            ]
        })

    def test_shell(self):
        self.assert_command({
            CMD: '-s',
            EXPECTATION: [
                'cd ./backend',
                'sqlite3 the.db'
            ]
        })