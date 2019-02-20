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

def apt_proxy(sudo_password, option, profile = ""):
    p = Popen(['sudo', '-S', './apt_proxy.py', option, profile], stdin=PIPE, stderr=PIPE, stdout= PIPE, universal_newlines=True)
    output, sudo_prompt = p.communicate(sudo_password + '\n')  
    return output, sudo_prompt

def get_apt_proxy():
    apt_config = {
        "enabled": False,
        "ftp":{
            "host":"",
            "port":""
        },
        "http":{
            "host":"",
            "port":""
        },
        "https":{
            "host":"",
            "port":""
        }
    }

    if not os.path.isdir('/etc/apt/apt.conf.d'):
        os.makedirs('/etc/apt/apt.conf.d')

    proxyConfPath = '/etc/apt/apt.conf.d/proxy.conf'
    if( os.path.isfile(proxyConfPath) ):
        with open(proxyConfPath) as fh:
            conf = fh.read()
            conf = conf.strip()
            # print(conf)
            # return
            if(conf == ''):
                apt_config["enabled"] = False
                return
            else:
                apt_config["enabled"] = True
                http = re.compile(r'Acquire::http::Proxy \"(.*):(\d+)\"')
                https = re.compile(r'Acquire::https::Proxy \"(.*):(\d+)\"')
                ftp = re.compile(r'Acquire::ftp::Proxy \"(.*):(\d+)\"')
                apt_config["http"]["host"],apt_config["http"]["port"] = http.findall(conf)[0]
                apt_config["https"]["host"],apt_config["https"]["port"] = https.findall(conf)[0]
                apt_config["ftp"]["host"],apt_config["ftp"]["port"] = ftp.findall(conf)[0]
                return apt_config
    else:
        return "no apt proxy file found"

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
    mode = os.popen("gsettings get org.gnome.system.proxy mode").read().strip()
    mode = mode[1:-1]
    return mode


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


# GUI METHODS

def getInfo():
    # skeleton
    config = {
        "git":{
            "enabled": False,
            "host": "",
            "port": "8080"
        },
        "system":{
            "enabled":False,
            "mode":"manual",
            "host":"1",
            "port":"8080"
        },
        "apt":{
            "enabled":False,
            "ftp":{
                "host":"",
                "port":"8080"
            },
            "http":{
                "host":"",
                "port":"8080"
            },
            "https":{
                "host":"",
                "port":"8080"
            }
        }
    }
    # apt
    config["apt"] = get_apt_proxy()
    # git
    git = get_git_proxy()
    if(git == ""):
        config["git"]["enabled"] = False
    else:
        config["git"]["enabled"] = False
        config["git"]["host"], config["git"]["port"] = git.split(":")
    # system
    config["system"]["mode"] = get_proxy_mode()
    if (config["system"]["mode"] == 'none'):
        config["system"]["enabled"] == False
    else:
        config["system"]["enabled"] == True
        config["system"]["host"], config["system"]["port"] == get_manual_proxy()

