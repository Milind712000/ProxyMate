#! /usr/bin/python3

import json

import tkinter as tk
import tkinter.messagebox
import os
from sys import exit
import proxy

# GUI

# funtions and classes

class Display:
    def __init__(self, window):
        self.InfoFrame = tk.Frame(window)
        self.InfoFrame.pack(side = "top", fill = "x")
        self.InnerFrame = tk.Frame(self.InfoFrame)
        self.InnerFrame.pack(side = "top", fill="x")

    def updateConfig(self):
        # complete this
        self.config = proxy.getInfo()
        self.profileName = "Kill Me Now"
        
    def sysProx(self, window, config):
        sysFrame = tk.Frame(window)
        sysFrame.pack(fill="x")
        tk.Label(sysFrame, text= ("System Proxy : "+str(config["enabled"]) ), font = ('arial',20,'bold') ).pack(fill="x")
        tk.Label(sysFrame, text= ("Mode : "+config["mode"] ) ).pack(fill="x")
        if(config["enabled"]):
            if(config['mode'] == 'manual'):
                tk.Label(sysFrame, text=("Host : "+config["host"]) ).pack(fill="x")
                tk.Label(sysFrame, text=("Port : "+config["port"]) ).pack(fill="x")
            elif(config['mode'] == 'auto'):
                tk.Label(sysFrame, text=("autoconfig-url : "+config["url"]) ).pack(fill="x")

    def aptProx(self, window, config):
        aptFrame = tk.Frame(window)
        aptFrame.pack(fill="x")
        tk.Label(aptFrame, text= ("apt Proxy : "+str(config["enabled"]) ), font = ('arial',20,'bold') ).pack(fill="x")
        if(config["enabled"]):
                http = config["http"]
                tk.Label(aptFrame, text="HTTP :" ).pack(fill="x")
                tk.Label(aptFrame, text=("Host : "+http["host"]) ).pack(fill="x")
                tk.Label(aptFrame, text=("Port : "+http["port"]) ).pack(fill="x")
                https = config["https"]
                tk.Label(aptFrame, text="HTTPS :" ).pack(fill="x")
                tk.Label(aptFrame, text=("Host : "+https["host"]) ).pack(fill="x")
                tk.Label(aptFrame, text=("Port : "+https["port"]) ).pack(fill="x")
                ftp = config["ftp"]
                tk.Label(aptFrame, text="FTP :" ).pack(fill="x")
                tk.Label(aptFrame, text=("Host : "+ftp["host"]) ).pack(fill="x")
                tk.Label(aptFrame, text=("Port : "+ftp["port"]) ).pack(fill="x")
            
    def gitProx(self, window, config):
        gitProx = tk.Frame(window)
        gitProx.pack(fill="x")
        tk.Label(gitProx, text= ("git Proxy : "+str(config["enabled"]) ), font = ('arial',20,'bold') ).pack(fill="x")
        if(config["enabled"]):
                tk.Label(gitProx, text=("Host : "+config["host"]) ).pack(fill="x")
                tk.Label(gitProx, text=("Port : "+config["port"]) ).pack(fill="x")

    def destroy(self):
        self.InfoFrame.destroy()

    def refresh(self):
        self.updateConfig()
        self.InnerFrame.destroy()

        self.InnerFrame = tk.Frame(self.InfoFrame)
        self.InnerFrame.pack(side = "top", fill="x")
        
        tk.Label(self.InnerFrame, text=self.profileName, font = ('arial',30,'bold'), fg = "red" ).pack(side="top",fill="x")
        self.sysProx(self.InnerFrame, self.config['system'])
        self.aptProx(self.InnerFrame, self.config['apt'])
        self.gitProx(self.InnerFrame, self.config['git'])


# window

root = tk.Tk()
root.title("ProxyMate")

#Info
Frame1 = tk.Frame(root, borderwidth = 1)

bottom_frame = tk.Frame(Frame1)
bottom_frame.pack(expand = True, fill = "both")

Info = Display(bottom_frame)

btn4 = tk.Button(bottom_frame, text = "Refresh", fg = "green", bg = "black", font = ("Arial Bold", 15), command = Info.refresh )
btn4.pack(side = "bottom", fill="x")

Info.refresh()
Frame1.pack(side = tk.LEFT)
#Info ends here

# change starts here

Frame3 = tk.Frame(root, borderwidth = 1)

if not os.path.isdir("profiles"):
    os.mkdir("profiles")

profiles = os.listdir("profiles")
profiles = [x[:-5] for x in profiles if x[-5:] == ".json"]


frame = tk.Frame(Frame3)
frame.pack(expand = True, fill = "both")

# if(len(profiles) == 0):
#     Frame3.destroy()
#     exit("No profiles Found")

selectedProfile = tk.StringVar()
if(len(profiles) == 0):
    tk.Label(Frame3, text = "No Profiles Found", font = ("Arial",30,"bold"), fg = "red" ).pack()
else:
    selectedProfile.set(profiles[0])

    tk.Label(frame, text = "Profile : ").grid(row = 0, column = 0)
    tk.OptionMenu(frame, selectedProfile, *profiles).grid(row = 0, column = 1)

    tk.Label(frame, text = "Password : ").grid(row = 1, column = 0)
    sudo_password = tk.Entry(frame, show = "*")
    sudo_password.grid(row = 1, column = 1)

def setProfile():
    profilePath = "./profiles/" + selectedProfile.get() + ".json"
    psk = sudo_password.get()
    proxy.setProfile(profilePath, psk)
    tk.messagebox.showinfo('Alert', ("profile was activated" ))

if(len(profiles) != 0 ):
    btn4 = tk.Button(Frame3, text = "SET", fg = "green", bg = "black", font = ("Arial Bold", 15), command = setProfile )
    btn4.pack(side = "bottom", fill="x")

Frame3.pack(side = tk.LEFT)

# change ends here



# add starts here

Frame2 = tk.Frame(root, borderwidth = 1)

tk.Label(Frame2, text = "Profile Name", font = ('arial',20,'bold')).pack()
profileName = tk.Entry(Frame2)
profileName.pack()


addFrame = tk.Frame(Frame2)
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

    tk.messagebox.showinfo('Alert', ("profile " + name + " was saved" + "\n Please Reload Application"))


btn4 = tk.Button(Frame2, text = "Add", fg = "green", bg = "black", font = ("Arial Bold", 15), command = Add )
btn4.pack(side = "bottom", fill="x")
Frame2.pack(side = tk.LEFT)

# add ends here

# root ends here


root.mainloop()