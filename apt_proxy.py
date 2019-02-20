#! /usr/bin/python3

# sudo apt_proxy.py (set|unset|get) host port
# host and port are required only for 'set'
# get is deprecated

import os
import re
import sys
import json

def set_apt_proxy(profilePath):
    config = ""
    if(os.path.isfile(profilePath)):
        with open(profilePath) as fh:
            config = json.load(fh)
    else:
        print("profile not found")
        return
    
    if not ( os.path.exists('/etc/apt/apt.conf.d') and os.path.isdir('/etc/apt/apt.conf.d') ):
        os.makedirs('/etc/apt/apt.conf.d')

    os.chdir('/etc/apt/apt.conf.d')
    config = config["apt"]
    with open('proxy.conf', 'w') as fh:
        fh.write('Acquire::http::Proxy \"{host}:{port}\";\n'.format(host = config["http"]["host"], port = config["http"]["port"]))
        fh.write('Acquire::https::Proxy \"{host}:{port}\";\n'.format(host = config["https"]["host"], port = config["https"]["port"]))
        fh.write('Acquire::ftp::Proxy \"{host}:{port}\";\n'.format(host = config["ftp"]["host"], port = config["ftp"]["port"]))

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

option = profilePath = ""
option = sys.argv[1]
if option == "set":
    profilePath = sys.argv[2]

if option == "set":
    set_apt_proxy(profilePath)
elif option == "unset":
    unset_apt_proxy()
elif option == "get":
    host, port = get_apt_proxy()
    print("Host :", host)
    print("Port :", port)
else:
    print("invalid option")