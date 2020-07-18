import argparse
import os

class CommandContext:

    def __init__(self, basedir, dry_run = False, printer=print, input_lines=None):
        self.basedir = basedir
        self.project_name = [s for s in basedir.split('/') if s][-1]
        self.dry_run = dry_run
        self.input_lines = input_lines
        self.printer = printer
        if input_lines:
            self.input_index = 0

    def rel_path(self, rel_path):
        return os.path.join(self.basedir, rel_path)

    def execute(self, command, rel_dir=None, abs_dir=None):
        cwd = os.getcwd()
        nwd = self.basedir
        if rel_dir:
            nwd = os.path.join(self.rel_path(rel_dir))
        elif abs_dir:
            nwd = abs_dir
        if nwd != cwd:
            self.print('cd ' + nwd)
        if not self.dry_run:
            os.chdir(nwd)

        shorter_command = ' '.join(s.strip() for s in command.split('\n'))
        self.print(shorter_command)
        if not self.dry_run:
            os.system(shorter_command)

    def new_context(self, basedir=None, dry_run=None, printer=None, input_lines=None):
        if basedir == None:
            basedir = self.basedir
        if dry_run == None:
            dry_run = self.dry_run
        if printer == None:
            printer = self.printer
        if input_lines == None:
            input_lines = self.input_lines[self.input_index:]

        return CommandContext(basedir, dry_run, printer, input_lines)

    def input(self, s):
        if self.input_lines:
            self.input_index += 1
            return self.input_lines[self.input_index - 1]

        return input(s)

    def print(self, *args):
        self.printer(' '.join([str(a) for a in args]))


class Command:
    name = ''
    description = ''
    context = None
    def __init__(self, context):
        self.context = context

    def add_args(parser):
        pass

    def main(args):
        pass

    def run(self, args):
        parser = argparse.ArgumentParser(description='''                                                                
 ,---.   ,--.           ,--.       ,--.             ,--.          
'   .-',-'  '-.,--. ,--.|  | ,---. |  |-.  ,--,--.,-'  '-. ,---.  
`.  `-.'-.  .-' \  '  / |  || .-. || .-. '' ,-.  |'-.  .-'| .-. : 
.-'    | |  |    \   '  |  |' '-' '| `-' |\ '-'  |  |  |  \   --. 
`-----'  `--'  .-'  /   `--' `---'  `---'  `--`--'  `--'   `----' 
               `---'                                              
_________________________________________________________________
{}
    '''.format(self.description), formatter_class=argparse.RawDescriptionHelpFormatter, prog='stylo ' + self.name)

        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='See what commands will be executed without actually executing them'
        )
        self.add_args(parser)

        parsed_args = parser.parse_args(args)

        if parsed_args.dry_run:
            self.context.dry_run = True

        self.main(parsed_args)


    def execute(self, command, rel_dir=None, abs_dir=None):
        self.context.execute(command, rel_dir, abs_dir)

    def print(self, *args):
        self.context.print(*args)

    def confirm(self, s):
        return self.input(s + '[Y/n]')[0].lower() == 'y'

    def input(self, s):
        return self.context.input(s + ': ')


