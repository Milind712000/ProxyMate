#! /usr/bin/python3

import tkinter as tk
import tkinter.messagebox
import os
import proxy

profiles = os.listdir("./profiles")
profiles = [x[:-5] for x in profiles if x[-5:] == ".json"]

root = tk.Tk()
root.title("ProxyMate")
root.geometry('600x700+500+100')


frame = tk.Frame(root)
frame.pack(expand = True, fill = "both")


selectedProfile = tk.StringVar()
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


btn4 = tk.Button(root, text = "SET", fg = "green", bg = "black", font = ("Arial Bold", 15), command = setProfile )
btn4.pack(side = "bottom", fill="x")

root.mainloop()