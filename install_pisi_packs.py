#import os
from os import system

def install_user_packs():
  userpacks=open("userpacks.lst","r")
  for line in userpacks:
    #os.system("sudo pisi it -y --reinstall %s" % line)
    system("sudo pisi it -y --reinstall %s" % line)
  userpacks.close() 
