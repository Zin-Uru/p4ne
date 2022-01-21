#!/usr/bin/python3

import glob
import ipaddress

folder = "/home/zinuru/PycharmProjects/pythonProject/Lab1.5/config_files/"
pat = "ip address"

flist = glob.glob(folder + "*.txt")

result = []

for i in flist:
    with open(i) as file:
        for j in file.readlines():
            if pat in j:
                splitted = j.strip().rstrip().split(" ")
                try:
                    addr1 = ipaddress.IPv4Address(splitted[2])
                    addr2 = ipaddress.IPv4Address(splitted[3])
                    result += [j, ]
                except (Exception, ):
                    pass

result = list(set(result))

for i in result:
    print(i, end="")
