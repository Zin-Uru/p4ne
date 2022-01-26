#!/usr/bin/python3

import requests
import paramiko
import time
import pprint

log = 'restapi'
pwd = 'j0sg1280-7@'
port = '55443'
buffer = 20000

ip1 = '10.31.70.209'
ip2 = '10.31.70.210'


def timeout(to=1):
    time.sleep(to)


ssh_con = paramiko.SSHClient()
ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_con.connect(ip1, username=log, password=pwd, look_for_keys=False, allow_agent=False)
session = ssh_con.invoke_shell()
session.send("\n")
timeout()
session.send("terminal length 0\n")
timeout(2)
session.send("show interfaces\r\n")
timeout()
s = session.recv(buffer).decode()
session.close()

result = {}
intf = ""
inp = ""
oup = ""

spl = s.split('\r\n')

for i in spl:
    if len(i.strip().rstrip().split(" ")) >= 4:
        words = i.strip().split(" ")
        if i[0] == i.strip()[0] and "#" not in i:
            intf = i.split(" ")[0]
        elif words[1] == 'packets' and words[2] == 'input,':
            inp = {"packets": words[0], "bytes": words[3]}
        elif words[1] == 'packets' and words[2] == 'output,':
            oup = {"packets": words[0], "bytes": words[3]}
        if intf != "" and inp != "" and oup != "":
            result.update({intf: {"input": inp, "output": oup}, })
            intf = ""
            inp = ""
            oup = ""

# for i in spl:
#   print(i)

for i in result:
    print(i, end=": ")
    start = True
    for j in "input", "output":
        for k in "packets", "bytes":
            if start:
                st = ""
                start = False
            else:
                st = ", "
            print(st + j + " " + k + " " + result[i][j][k], end="")
    print()

"""
url = 'https://' + ip2 + ':' + port + '/api/v1/auth/token-services'
req = requests.post(url,  auth=(log, pwd), verify=False)
if req.status_code == 200:
    token = req.json()['token-id']
    head = {"content-type": "application/json", "X-Auth-Token": token}
    url2 = 'https://' + ip2 + ':' + port + '/api/v1/interfaces'
    req = requests.get(url2, headers=head, verify=False)
else:
    print("Can't proceed: " + str(req.status_code) + " code")
"""
