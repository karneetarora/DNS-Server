import socket

class Hostname():
    def __init__(self, host, ip_address, flag):
        self.host = host
        self.ip_address = ip_address
        self.flag = flag

table = []
file = open("PROJI-DNSTS.txt", "r")
for line in file:
    host, ip, flag = line.split()
    host_name = Hostname(host, ip, flag)
    table.append(host_name)

def lookup(hostname):
    found = False
    for i in table:
        if i.host == hostname:
            found = True
            return f'{i.host} {i.ip_address} {i.flag}'
    if not found:
        pass

