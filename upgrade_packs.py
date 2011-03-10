#!/usr/bin/python
from pisi.api import list_upgradable
from pisi.api import get_upgrade_order
from pisi.api import get_base_upgrade_order
from pisi.api import upgrade

def upgrade_pisi_packs():
  """ Pisideki guncellenebilir paketleri gunceller """
  up_list = list_upgradable()
  #print up_list
  
  if up_list == []:
    print "nothing to upgrade!\n"
    return 
  
  guo = get_upgrade_order(up_list)
  #print guo
  
  gbuo = get_base_upgrade_order(up_list)
  #print gbuo
  
  upgrade(gbuo)#system packs
  upgrade(guo)#pisi packs
  print "done!\n"