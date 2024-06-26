import sys
import os
from utils import *
import tabulate
from command import Command

class CLI:

    def __init__(self):
        self.dir = os.getcwd()
        self.log = None
        # self.log = self.init_log()
        # self.record_initial_data()
        self.prompt = '-:'
        self.recording = False
        self.running = True
        self.cmdline = ''

        self.cmdmap = {'encsearch': encoding_search}

        self.run()

    def run(self):
        print('WELCOME')
        while self.running:
            cmd = self.get_command()
            self.execute_command(cmd)
        self.quit()

    def quit(self):
        print('EXITING')
        if self.log is not None:
            self.log.close()

    def parse_command(self):
        cmd = [self.cmdline]
        if ' ' in self.cmdline:
            cmd = self.cmdline.split()
        return cmd

    def get_command(self):
        self.cmdline = input(self.prompt + ' ')
        return self.parse_command()

    def execute_command(self, cmd):
        if cmd[0] == 'q':
            self.running = False
            return
        results = self.cmdmap[cmd[0]](*cmd[1:])
        if cmd[0] == 'encsearch':
            # results = encoding_search(cmd[1], cmd[2])
            self.display_results(results, headers=['enc1', 'enc2', 'found'])

    def display_results(self, results, headers=None):
        table = tabulate.tabulate(results, headers=headers)
        print(table)

    def record_initial_data(self):
        # boilerplate for log file
        self.log.write('SESSION LOG')
        self.log.write(f'  timestamp: {get_datetime_string(raw=True)}')

    def init_log(self):
        # check if log folder exists, create it if not
        logfolder = os.path.join(self.dir, 'log')
        if not os.path.exists(logfolder):
            os.makedirs(logfolder)

        # get datetime string and create filename from it
        now = get_datetime_string()
        name = os.path.join(logfolder, now + '.log')
        return open(name, 'w')