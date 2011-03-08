from pisi.api import list_repos
from pisi.api import update_repos

def update_pisi_repositories():
  rp_list = []
  rp_list = list_repos(True)
  update_repos(rp_list, False)