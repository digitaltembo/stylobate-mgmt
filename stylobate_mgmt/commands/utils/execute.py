import os

def execute(command, wd=None):
    if wd:
        if isinstance(wd, str):
            os.chdir(wd)
        else:
            os.chdir(os.path.join(*wd))
    shorter_command = ' '.join(s.strip() for s in command.split('\n'))
    print(shorter_command)
    os.system(shorter_command)