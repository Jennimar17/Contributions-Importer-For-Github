# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo(r"C:\Users\jenni\Documents\UALABEE\CMS\site-ualabee-cms-3")
# Your mock repo
mock_repo = git.Repo(r"C:\Users\jenni\Documents\contributions3\Contributions-Importer-For-Github")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['jennimar17@gmail.com', 'jeniffer@ualabee.com', '62664863+Jennimar17@users.noreply.github.com'])
importer.import_repository()
# pip3 install gitpython
# pip3 install pathlib 
# run ✗ python3 run_script.py