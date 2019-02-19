import os
import re
from subprocess import Popen, PIPE

# GUIDELINES
# dont run this whole script with root privileges
# if gsettings is run with root privileges then the settings don't persist

# GENERAL TODO
# use subprocess module insted of os.popen and os.system

# APT PROXY

# TODO
# backup and remove apt.conf
# backup proxy.conf before changing its contents
# unset apt proxy
# set different proxy for http, https, ftp

def apt_proxy(sudo_password, option, host = "", port = ""):
    p = Popen(['sudo', '-S', './apt_proxy.py', option, host, port], stdin=PIPE, stderr=PIPE, stdout= PIPE, universal_newlines=True)
    output, sudo_prompt = p.communicate(sudo_password + '\n')  
    return output, sudo_prompt

# GIT PROXY

# TODO
# check if git is present

def set_git_proxy(Host,Port):
    os.system("git config --global http.proxy {host}:{port}".format(host = Host, port = Port))

def unset_git_proxy():
    os.system("git config --global --unset http.proxy")

def get_git_proxy():
    return os.popen("git config --global --get http.proxy").read().strip()


# PROXY MODE

def set_proxy_mode(Mode):
    # Mode can be 'none', 'auto' or 'manual' :: quotes are included so its like "'auto'"
    os.system("gsettings set org.gnome.system.proxy mode  '{mode}'".format(mode = Mode))
    # os.system("./set_proxy_mode.sh '{mode}'".format(mode = Mode))


def get_proxy_mode():
    return os.popen("gsettings get org.gnome.system.proxy mode").read().strip()


# CHANGE SYSTEM_WIDE PROXY

# AUTO

def set_autoconfig_url(URL):
    os.system("gsettings set org.gnome.system.proxy autoconfig-url {url}".format(url = URL))
    # os.system("./set_autoconfig_url.sh {url}".format(url = URL))

def get_autoconfig_url():
    return os.popen("gsettings get org.gnome.system.proxy autoconfig-url").read().strip()

# MANUAL

def set_manual_proxy(Host, Port):
    # set host
    os.system("gsettings set org.gnome.system.proxy.http host {host}".format(host = Host) )     # http
    os.system("gsettings set org.gnome.system.proxy.https host {host}".format(host = Host) )    # https
    os.system("gsettings set org.gnome.system.proxy.ftp host {host}".format(host = Host) )      # ftp
    os.system("gsettings set org.gnome.system.proxy.socks host {host}".format(host = Host) )    # socks
    # set port
    os.system("gsettings set org.gnome.system.proxy.http port {port}".format(port = Port) )     # http
    os.system("gsettings set org.gnome.system.proxy.https port {port}".format(port = Port) )    # https
    os.system("gsettings set org.gnome.system.proxy.ftp port {port}".format(port = Port) )      # ftp
    os.system("gsettings set org.gnome.system.proxy.socks port {port}".format(port = Port) )    # socks
    # os.system('./set_manual_proxy.sh {host} {port}'.format(host = Host, port = Port))
    
def get_manual_proxy():
    Host = os.popen("gsettings get org.gnome.system.proxy.http host").read().strip()
    Port = os.popen("gsettings get org.gnome.system.proxy.http port").read().strip()
    return Host, Port