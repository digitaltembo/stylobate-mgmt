from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext
from .command_test import CommandTest, CMD, INPUT, EXPECTATION, NAME

class InitTest(CommandTest):
    command = 'init'
    # def test_sample(self):
    #     self.gen_cmds([
    #         {CMD:'sample_proj X', NAME: 'init', INPUT:['test_git_user', 'test_user', 'test_pass']},
    #     ])

    def test_init(self):
        self.assert_command({
            CMD: 'sample_proj X',
            INPUT: [
                'test_git_user',
                'test_user',
                'test_pass'
            ],
            EXPECTATION: [
                'Initializing new project sample_proj in directory X',
                'cd X',
                'gh repo create -d "Stylobate-based Web Application" sample_proj',
                'cd X/sample_proj',
                'mkdir sample_proj',
                'cd X/sample_proj',
                'git init',
                'cd X/sample_proj',
                'git remote add origin git@github.com:test_git_user/sample_proj.git',
                'cd X/sample_proj',
                'git remote add upstream git@github.com:digitaltembo/stylobate.git',
                'cd X/sample_proj',
                'git pull upstream master',
                'cd X/sample_proj',
                'git push -u origin master',
                'cd X/sample_proj/backend',
                'python -m venv venv',
                'cd X/sample_proj/backend',
                'venv/bin/pip install -r requirements.txt',
                'cd X/sample_proj/frontend',
                'yarn install',
                'cd X/sample_proj/backend',
                'sqlite3 the.db "$(venv/bin/python -c "from db.models import User; User.create_superuser(\'test_user\', \'test_pass\')")"'
            ]
        })