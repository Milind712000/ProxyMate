#! /usr/bin/python3

# sudo apt_proxy.py (set|unset|get) host port
# host and port are required only for 'set'

import os
import re
import sys

def set_apt_proxy(Host,Port):
    if not ( os.path.exists('/etc/apt/apt.conf.d') and os.path.isdir('/etc/apt/apt.conf.d') ):
        os.makedirs('/etc/apt/apt.conf.d')

    os.chdir('/etc/apt/apt.conf.d')

    with open('proxy.conf', 'w') as fh:
        fh.write('Acquire::http::Proxy \"{host}:{port}\";\n'.format(host = Host, port = Port))
        fh.write('Acquire::https::Proxy \"{host}:{port}\";\n'.format(host = Host, port = Port))
        fh.write('Acquire::ftp::Proxy \"{host}:{port}\";\n'.format(host = Host, port = Port))

def get_apt_proxy():
    Host = Proxy = ""

    if not os.path.isdir('/etc/apt/apt.conf.d'):
        os.makedirs('/etc/apt/apt.conf.d')

    os.chdir('/etc/apt/apt.conf.d')

    if( os.path.isfile('proxy.conf') ):
        with open('proxy.conf') as fh:
            regex = re.compile(r'Acquire::http::Proxy \"(.*):(\d+)\"')
            result = regex.findall(fh.readline())
            if (len(result)):
                Host, Proxy = result[0]
            else:
                Host = Proxy = "empty"
        return Host, Proxy
    else:
        return "no apt proxy file found"

def unset_apt_proxy():
    if not ( os.path.exists('/etc/apt/apt.conf.d') and os.path.isdir('/etc/apt/apt.conf.d') ):
        os.makedirs('/etc/apt/apt.conf.d')

    os.chdir('/etc/apt/apt.conf.d')

    with open('proxy.conf', 'w') as fh:
        fh.write('\n')

option = host = port = ""
option = sys.argv[1]
if option == "set":
    host = sys.argv[2]
    port = sys.argv[3]

if option == "set":
    set_apt_proxy(host,port)
elif option == "unset":
    unset_apt_proxy()
elif option == "get":
    host, port = get_apt_proxy()
    print("Host :", host)
    print("Port :", port)
else:
    print("invalid option")