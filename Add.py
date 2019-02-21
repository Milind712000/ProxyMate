#! /usr/bin/python3

import tkinter as tk
import tkinter.messagebox
import proxy
import json

# GUI

root = tk.Tk()
root.title("ProxyMate")
root.geometry('500x700+1100+100')

tk.Label(root, text = "Profile Name", font = ('arial',20,'bold')).pack()
profileName = tk.Entry(root)
profileName.pack()


addFrame = tk.Frame(root)
addFrame.pack(expand = True, fill = "x")

# apt proxy

tk.Label(addFrame, text = "Apt Proxy :", font = ('arial',20,'bold')).grid(row = 0, column = 0)
apt_enabled = tk.BooleanVar()
tk.Checkbutton(addFrame, text="enabled", var = apt_enabled).grid(row = 1, column = 0)

httpFrame = tk.Frame(addFrame)
httpFrame.grid(row = 2, column = 0, columnspan = 2)

tk.Label(httpFrame, text = "http Proxy :").grid(row = 0, column = 0)
tk.Label(httpFrame, text = "Host").grid(row = 2, column = 0)
apt_http_host = tk.Entry(httpFrame)
apt_http_host.grid(row = 2, column = 1)
tk.Label(httpFrame, text = "Port").grid(row = 3, column = 0)
apt_http_port = tk.Entry(httpFrame)
apt_http_port.grid(row = 3, column = 1)

httpsFrame = tk.Frame(addFrame)
httpsFrame.grid(row = 3, column = 0, columnspan = 2)

tk.Label(httpsFrame, text = "https Proxy :").grid(row = 0, column = 0)
tk.Label(httpsFrame, text = "Host").grid(row = 2, column = 0)
apt_https_host = tk.Entry(httpsFrame)
apt_https_host.grid(row = 2, column = 1)
tk.Label(httpsFrame, text = "Port").grid(row = 3, column = 0)
apt_https_port = tk.Entry(httpsFrame)
apt_https_port.grid(row = 3, column = 1)

ftpFrame = tk.Frame(addFrame)
ftpFrame.grid(row = 4, column = 0, columnspan = 2)

tk.Label(ftpFrame, text = "ftp Proxy :").grid(row = 0, column = 0)
tk.Label(ftpFrame, text = "Host").grid(row = 2, column = 0)
apt_ftp_host = tk.Entry(ftpFrame)
apt_ftp_host.grid(row = 2, column = 1)
tk.Label(ftpFrame, text = "Port").grid(row = 3, column = 0)
apt_ftp_port = tk.Entry(ftpFrame)
apt_ftp_port.grid(row = 3, column = 1)

# systemProxy

tk.Label(addFrame, text = "System Proxy :", font = ('arial',20,'bold')).grid(row = 5, column = 0)
sys_enabled = tk.BooleanVar()
tk.Checkbutton(addFrame, text="enabled", var = sys_enabled).grid(row = 6, column = 0)
sys_mode = tk.StringVar()

sysFrame = tk.Frame(addFrame)
sysFrame.grid(row = 7, column = 0, columnspan = 2)

tk.Radiobutton(sysFrame, text="none", var = sys_mode, value = "none").grid(row = 1, column = 1  )
tk.Radiobutton(sysFrame, text="manual", var = sys_mode, value = "manual").grid(row = 1, column = 2 )
tk.Radiobutton(sysFrame, text="auto", var = sys_mode, value = "auto").grid(row = 1, column = 3 )

tk.Label(sysFrame, text = "Host").grid(row = 2, column = 0)
sys_host = tk.Entry(sysFrame)
sys_host.grid(row = 2, column = 1)
tk.Label(sysFrame, text = "Port").grid(row = 3, column = 0)
sys_port = tk.Entry(sysFrame)
sys_port.grid(row = 3, column = 1)
tk.Label(sysFrame, text = "Auto-Config Url").grid(row = 4, column = 0)
sys_url = tk.Entry(sysFrame)
sys_url.grid(row = 4, column = 1)

# git

tk.Label(addFrame, text = "Git Proxy :", font = ('arial',20,'bold')).grid(row = 8, column = 0)
git_enabled = tk.BooleanVar()
tk.Checkbutton(addFrame, text="enabled", var = git_enabled).grid(row = 9, column = 0)

gitFrame = tk.Frame(addFrame)
gitFrame.grid(row = 10, column = 0, columnspan = 2)

tk.Label(gitFrame, text = "Host").grid(row = 2, column = 0)
git_host = tk.Entry(gitFrame)
git_host.grid(row = 2, column = 1)
tk.Label(gitFrame, text = "Port").grid(row = 3, column = 0)
git_port = tk.Entry(gitFrame)
git_port.grid(row = 3, column = 1)

def Add():
    config = {
        "git":{
            "enabled": False,
            "host": "",
            "port": ""
        },
        "system":{
            "enabled":False,
            "mode":"auto|none|manual",
            "host":"",
            "port":"",
            "url":""
        },
        "apt":{
            "enabled":False,
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
    }
    config["git"]["enabled"] = bool(git_enabled.get())
    config["git"]["host"] = git_host.get()
    config["git"]["port"] = git_port.get()

    config["system"]["enabled"] = bool(sys_enabled.get())
    config["system"]["mode"] = str(sys_mode.get())
    config["system"]["url"] = sys_url.get()
    config["system"]["host"] = sys_host.get()
    config["system"]["port"] = sys_port.get()

    if(config["system"]["mode"] == "none"):
        config["system"]["enabled"] = False

    config["apt"]["enabled"] = bool(apt_enabled.get())

    config["apt"]["http"]["host"] = apt_http_host.get()
    config["apt"]["http"]["port"] = apt_http_port.get()

    config["apt"]["https"]["host"] = apt_https_host.get()
    config["apt"]["https"]["port"] = apt_https_port.get()

    config["apt"]["ftp"]["host"] = apt_ftp_host.get()
    config["apt"]["ftp"]["port"] = apt_ftp_port.get()

    name = profileName.get()
    #check and see that profile name has no spaces or it will cause problems in sudo apt_proxy.py argument list

    with open("./profiles/"+name+".json", "w") as fh:
        json.dump(config, fh, indent=4)

    tk.messagebox.showinfo('Alert', ("profile " + name + " was saved" ))


btn4 = tk.Button(root, text = "Add", fg = "green", bg = "black", font = ("Arial Bold", 15), command = Add )
btn4.pack(side = "bottom", fill="x")
root.mainloop()