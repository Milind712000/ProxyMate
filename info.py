import tkinter as tk
import proxy
import json

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
        tk.Label(sysFrame, text= ("System Proxy : "+str(config["enabled"]) ) ).pack(fill="x")
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
        tk.Label(aptFrame, text= ("apt Proxy : "+str(config["enabled"]) ) ).pack(fill="x")
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
        tk.Label(gitProx, text= ("git Proxy : "+str(config["enabled"]) ) ).pack(fill="x")
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
        
        tk.Label(self.InnerFrame, text=self.profileName).pack(side="top",fill="x")
        self.sysProx(self.InnerFrame, self.config['system'])
        self.aptProx(self.InnerFrame, self.config['apt'])
        self.gitProx(self.InnerFrame, self.config['git'])

root = tk.Tk()
root.title("ProxyMate")
root.geometry('400x600+800+200')


bottom_frame = tk.Frame(root)
bottom_frame.pack(expand = True, fill = "both")

Info = Display(bottom_frame)

btn4 = tk.Button(bottom_frame, text = "Refresh", fg = "green", bg = "black", font = ("Arial Bold", 15), command = Info.refresh )
btn4.pack(side = "bottom", fill="x")

root.mainloop()