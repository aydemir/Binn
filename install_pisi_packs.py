#!/usr/bin/python
from pisi.api import get_install_order
from pisi.api import get_conflicts
from pisi.api import install

def install_user_packs():
  print "Getting list of packages"
  f=open("userpacks.lst","r")
  temp_list = []
  map(lambda x: temp_list.append(x.strip("\n")), f)
  f.close()
  
  print "Install order is being determined"
  install_order_list = get_install_order(temp_list)
  print "Installation begins! Please wait..."
  #def install(packages, reinstall=False, ignore_file_conflicts=False, ignore_package_conflicts=False):
  flag = install(install_order_list, False, False, False)
  
  if flag == True:
    print "All of the packages are installed successfully! (:"
    return True
  else:
    print "Bad times! Packages couldnt installed successfully! :("
    return False