#!/usr/bin/python
#-*-coding: utf-8-*-
""" --- Binn --- """
from exp_imp_pisi_packs import import_installed_packages
from exp_imp_pisi_packs import export_installed_packages
from install_pisi_packs import install_user_packs
from update_repos import update_pisi_repositories
from upgrade_packs import upgrade_pisi_packs

def extract_pack():
  """ Gets installed Pisi packages by user named userpacks """
  print "Starting..."
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
  print "Finished!"

def menuPrinting():
  """ User menu of Binn application """
  print '=' * 9 + ' MENU ' + '=' * 9
  print '1-Update repository'
  print '2-Update Pisi'
  print '3-Extract package list from Pisi'
  print '4-Setup packages'
  print '0-Exit'
  print '=' * 24

def executeCode(ch):
  """ Menu choices """
  if ch == 1:
    update_pisi_repositories()
  elif ch == 2:
    upgrade_pisi_packs()
  elif ch == 3:
    extract_pack()
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
    print "WRONG! Enter a NUMBER!\n"
    continue
  elif int(choice) > upperchoice or int(choice) < lowerchoice:
    print "WRONG! Enter a VALID number!\n"
    continue
  else:
    executeCode(int(choice))