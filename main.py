import os
import sys
import re
import subprocess

from programs import port_scanner, submarine, boat


class Lead:
    """Lead tools"""

    def __init__(self, arg):
        super(Lead, self).__init__()
        self.arg = arg

    def deliverance(self, function_to_call):
        subprocess.call('clear', shell=True)
        function_to_call(self.split(' ')[1:])
        command = input()
        Lead.main(command)

    def main(self):
        if any(map(self.__contains__, programs)):
            if 'portscan' in self:
                Lead.deliverance(self, port_scanner)
            elif 'submarine' in self:
                Lead.deliverance(self, submarine)
            elif 'boat' in self:
                Lead.deliverance(self, boat)
        elif self in call_for_help:
            for count, i in enumerate(programs):
                print(f'[*] {i} Usage : {i} {usage[count]}')
            command = input()
            Lead.main(command)


if __name__ == '__main__':
    call_for_help = ['help', 'h', '-h', '--help', 'man', '/?']
    programs = ['cspider', 'portscan', 'urlfind', 'brutedog', 'gang', 'submarine', 'boat']
    usage = ['url', 'ip', 'url', 'ip port username password.list', 'ip port', 'url', 'url']
    nfo = """
           )
       ____(_
       |____|
       |    |     Welcome to Lead
       (____|      CTF helper.
     ==========
      /  ()  \\
     /   ||   \\
    /   _||_   \\
    """

    print(f"{nfo}\n[~] Type help for more info or run your sexy programs")
    cmd = str(input())
    Lead.main(cmd)
