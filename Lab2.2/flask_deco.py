#!/usr/bin/python3

from flask import Flask
from flask import jsonify
import glob
import ipaddress
import re


class Getinfo:
    def __init__(self, line):
        self.line = line.strip().rstrip()

    def mkdict(self):
        if bool(re.match('^ip address( ([0-9]{1,3}\.){3}[0-9]{1,3}){2}$', self.line)):
            return {"ip": ipaddress.IPv4Interface((self.line.split(" ")[2], self.line.split(" ")[3]))}
        elif bool(re.match('^interface ([a-zA-Z0-9\.\-\/]+){1}$', self.line)):
            return {"int": self.line.split(" ")[1]}
        elif bool(re.match('^hostname ([a-zA-Z0-9\.\-]+){1}$', self.line)):
            return {"host": self.line.split(" ")[1]}
        else:
            return {}


folder = "/home/zinuru/PycharmProjects/pythonProject/Lab1.5/config_files/"

flist = glob.iglob(folder + "*.txt")

hostinfo = {}

for i in flist:
    with open(i) as file:
        ips = []
        ints = []
        hosts = []
        for j in file.readlines():
            result = Getinfo(j).mkdict()
            if result == {}:
                pass
            elif list(result)[0] == 'ip':
                ips += [str(result['ip']), ]
            elif list(result)[0] == 'int':
                ints += [result['int'], ]
            elif list(result)[0] == 'host':
                if list(result) not in hosts:
                    hosts += [result['host'], ]
        hostinfo.update({hosts[0]: ips})

"""
for i in list(hostinfo):
    adr = hostinfo[i]
    for j in adr:
        print(i + " " + j)
"""

app = Flask('__name__')


@app.route('/')
def p_help():
    return "This is Help maybe"


@app.route('/config')
def p_hosts():
    return jsonify(tuple(hostinfo.keys()))


@app.route('/config/<hostname>')
def p_ips(hostname):
    if hostname in hostinfo.keys():
        return jsonify(hostinfo[hostname])
    else:
        return "Oops! Wrong host"


if __name__ == '__main__':
    app.run(debug=True)
