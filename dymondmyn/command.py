import os


class CommandModule:

    def __init__(self, parent):

        self.parent = parent

        self.cmds = {'cat': self.cat,
                     'cd': self.cd,
                     'echo': self.echo,
                     'ls': self.ls,
                     'sublime': self.sublime
                     }
        self.reqs = {'cat': {'num': [1]},
                     'cd': {'num': [1]},
                     'echo': {'num': [1]},
                     'ls': {'num': [0, 1]},
                     'sublime': {'num': [0]}
                     }

    def exec(self, cmd):
        cmd = cmd.split()
        if self.check_tokens(cmd):
            self.cmds[cmd[0]](*cmd[1:])
        else:
            self.parent.console_log(f'> incorrect usage of command [{cmd[0]}]', err=True)

    def check_tokens(self, cmd):
        if cmd[0] in self.cmds:
            if len(cmd[1:]) in self.reqs[cmd[0]]['num']:
                return True
            return False
        return False

    def ls(self, d=None):
        print('ls', d)

    def cd(self, d):
        try:
            os.chdir(d)
            self.parent.console_log(f'changed to {os.getcwd()}')
            self.parent.statusBar().showMessage(f'{os.getcwd()}\t\t\tmain display: command line log')
        except Exception as e:
            self.parent.console_log(f'> {e}', err=True)

    def cat(self, name):
        print(name)

    def echo(self, s):
        print(s)

    def sublime(self):
        os.chdir(r'C:\\Program Files\\Sublime Text')
        os.system('sublime_text.exe')