#-*-coding: utf-8-*-
from pisi.api import list_upgradable
from pisi.api import get_upgrade_order
from pisi.api import get_base_upgrade_order
from pisi.api import upgrade

def upgrade_pisi_packs():
  """ Pisideki guncellenebilir paketleri gunceller """
  print "Upgrading process may take several minutes with respect to number of upgradable packages! Please wait..."
  up_list = list_upgradable()
    
  if up_list == []:
    print "Nothing to upgrade!"
    return False
    
  else:
    print "Upgradable packages:"
    for i in up_list:
      print i,
    
    print "Getting order list of upgradable system packages"
    guo = get_upgrade_order(up_list)
    #print guo
    print "Getting order list of upgradable user packages"
    gbuo = get_base_upgrade_order(up_list)
    #print gbuo
    print "Updating system packages! Please wait..."
    upgrade(gbuo)#system packs
    print "Updating user packages! Please wait..."
    upgrade(guo)#pisi packs
    return True