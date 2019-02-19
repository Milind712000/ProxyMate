from tkinter import *
from proxy import *

root = Tk()


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








# CurrentSettings = Frame(root)
# CurrentSettings.pack(side = TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM, fill = X)

root.mainloop()