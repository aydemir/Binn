#!/usr/bin/python
from pisi.api import get_install_order
from pisi.api import get_conflicts
from pisi.api import install

def install_user_packs():
  userpacks=open("userpacks.lst","r")
  temp_list = []
  for line in userpacks:#put packs into a list
    temp_list.append(line)
  userpacks.close()

  install_order_list = get_install_order(temp_list)
  print install_order_list
  #def install(packages, reinstall=False, ignore_file_conflicts=False, ignore_package_conflicts=False):
  flag = install(install_order_list, False, False, False)
  print flag
  if flag == True:
    print "All of the packages are installed successfully! (:\n"
    return True
  else:
    print "Bad times! Packages couldnt installed successfully! :(\n"
    return False