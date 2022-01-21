#!/usr/bin/python3

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
# pat = "ip address"

flist = glob.iglob(folder + "*.txt")

# result = []
ips = []
ints = []
hosts = []

for i in flist:
    with open(i) as file:
        for j in file.readlines():
            """
            if pat in j:
                splitted = j.strip().rstrip().split(" ")
                try:
                    ipaddress.IPv4Address(splitted[2])
                    ipaddress.IPv4Address(splitted[3])
                    result += [j, ]
                except (Exception, ):
                    pass
            """
            result = Getinfo(j).mkdict()
            if result == {}:
                pass
            elif list(result)[0] == 'ip':
                ips += [result['ip'], ]
            elif list(result)[0] == 'int':
                ints += [result['int'], ]
            elif list(result)[0] == 'host':
                hosts += [result['host'], ]

"""
result = list(set(result))

for i in result:
    print(i, end="")
"""

ips = list(set(ips))
ints = list(set(ints))
hosts = list(set(hosts))

print("IP addresses:")
start = True
for i in ips:
    if start:
        print(i, end="")
        start = False
    else:
        print(", " + str(i), end="")
print("\n")

print("Interfaces:")
start = True
for i in ints:
    if start:
        print(i, end="")
        start = False
    else:
        print(", " + i, end="")
print("\n")

print("Hosts:")
start = True
for i in hosts:
    if start:
        print(i, end="")
        start = False
    else:
        print(", " + i, end="")
print("\n")
