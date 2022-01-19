#!/usr/bin/python3

from pysnmp.hlapi import *

g = getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('10.31.70.107', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

n = nextCmd(SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('10.31.70.107', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
            lexicographicMode=False)

print(type(g))
print(type(n))

for r in g:
    for e in r[3]:
        print(e)

for r in n:
    for e in r[3]:
        print(e)
