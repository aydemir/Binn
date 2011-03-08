#!/usr/bin/env python
""" --- Pardus Online Paket Yukleme --- """
import os
from pisi.db.installdb import InstallDB
from exp_imp_pisi_packs import import_installed_packages
from exp_imp_pisi_packs import export_installed_packages
from install_pisi_packs import install_user_packs
from update_repos import update_pisi_repositories

def extractPack():
  """ Gets installed Pisi packages by user named userpacks """
  os.system("echo Starting...\n")
  export_installed_packages()
  imported_list = []
  import_installed_packages(imported_list)

  corepacks = open("corepacks","r")#put core packages into another list
  corep = []
  for line in corepacks:
    packname = line.split()
    corep.append(packname[0])
  corepacks.close()
  
  userpacks = open("userpacks.lst","w")
  #compare lists  
  for line in imported_list:
    if line not in corep:
      userpacks.write(line+"\n")
  userpacks.close()
  os.system("echo Done!\n")

def menuPrinting():
  print '\n' + '=' * 9 + ' MENU ' + '=' * 9
  print '1-Update repository'
  print '2-Update Pisi'
  print '3-Extract package list from Pisi'
  print '4-Setup packages'
  print '0-Exit\n'

def executeCode(ch):
  if ch == 1:
    update_pisi_repositories()
    os.system("echo Updating repository is done!")
  elif ch == 2:
    os.system("sudo pisi up")
  elif ch == 3:
    extractPack()
  elif ch == 4:
    install_user_packs()
  elif ch == 0:
    exit()

choice = 1
# menu
while choice != 0:
  menuPrinting()
  choice = raw_input("Select one of them!\t")
  upperchoice=4
  lowerchoice=0
  
  if choice.isdigit() != True:
    os.system("echo WRONG! Enter a NUMBER!\n")
    continue
  elif int(choice) > upperchoice or int(choice) < lowerchoice:
    os.system("echo WRONG! Enter a VALID number!\n")
    continue
  else:
    executeCode(int(choice))