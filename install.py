#! /usr/bin/python3

import os

os.system("chmod +x apt_proxy.py")
os.system("chmod +x launch")

# fix path in .desktop files
Path = os.getcwd()
with open("ProxyMate.desktop","w") as fh:
    with open("desktopTemplate", "r") as template:
        fh.write(template.read())
    fh.write("\nPath={path}/\n".format(path = Path))
    fh.write("Exec={path}/launch\n".format(path = Path))

os.system("chmod +x ProxyMate.desktop")

os.system("cp ProxyMate.desktop ~/.local/share/applications/")
