#!/usr/bin/python3

from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self, mstart=0, mend=32):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(mstart, mend)), strict=False)

    def regular(self):
        return self.is_global and not self.is_private


netlist = []

while len(netlist) < 10:
    net = IPv4RandomNetwork(8, 24)
    if net.regular() and net not in netlist:
        netlist.append(net)

for i in netlist:
    print(i)
