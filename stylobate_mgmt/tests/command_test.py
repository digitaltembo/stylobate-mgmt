from unittest import TestCase

from stylobate_mgmt.stylo import run
from stylobate_mgmt.commands.utils import CommandContext

EXPECTATION = 'expectation'
CMD = 'cmd'
INPUT = 'stdin'
NAME = 'name'

class CommandTest(TestCase):
    command = ''

    def run_cmd(self, cmd):
        args = cmd[CMD].split(' ') + ['--dry-run']
        output_lines = []
        input_lines = [] if not INPUT in cmd else cmd[INPUT]

        context = CommandContext('.', input_lines=input_lines, printer=output_lines.append)
        run(self.command, context, args)
        return output_lines

    def assert_command(self, cmd):
        output_lines = self.run_cmd(cmd)
        self.assertEqual(output_lines, cmd[EXPECTATION])

    def gen_cmds(self, cmds):
        for cmd in cmds:
            expectation = self.run_cmd(cmd)
            input_line = ''
            if INPUT in cmd:
                input_line = self.pretty_array('INPUT', cmd[INPUT]) + ','

            print('''
    def test_{}(self):
        self.assert_command({{
            CMD: '{}',{}{}
        }})'''.format(cmd[NAME], cmd[CMD], input_line, self.pretty_array('EXPECTATION', expectation)))
        self.assertTrue(False)

    def pretty_array(self, title, arr):
        return '''
            {}: [
                {}
            ]'''.format(title, ',\n                '.join(["'{}'".format(a) for a in arr]))


