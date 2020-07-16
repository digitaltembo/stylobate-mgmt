import argparse

class Command:
    name = ''
    description = ''

    def add_args(parser):
        pass

    def main(args, basedir):
        pass

    def execute(self, args, basedir):
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

        self.add_args(parser)

        parsed_args = parser.parse_args(args)
        self.main(parsed_args, basedir)

