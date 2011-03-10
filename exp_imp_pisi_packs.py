#!/usr/bin/python
from pisi.api import list_installed

def export_installed_packages():
  """ It exports packages to a file named installed_packages.lst """
  print "Getting list of installed packages from Pisi"
  installed_packages = list_installed()
  installed_packages.sort()
  print "Writing list to a file named installed_packages.lst"
  f = open("installed_packages.lst", "w")
  map(lambda x: f.write("%s\n" % x), installed_packages)
  f.close()
  print "Done!"
  return True

def import_installed_packages(imported_list):
  """ It imports packages to a list named imported_list from file named installed_packages.lst """
  print "Getting list of installed packages from file named installed_packages.lst"
  source_file = "installed_packages.lst"
  f = open(source_file, "r")
  map(lambda x: imported_list.append(x.strip("\n")), f)
  f.close()
  print "Done!"
  return imported_list