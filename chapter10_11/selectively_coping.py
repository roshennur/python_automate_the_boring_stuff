import os, re, shutil
from pathlib import Path

h = Path.home()
folder = h / 'select'
selected = h / 'selected'
(h / 'selected').mkdir(exist_ok = True)

pattern = re.compile('.*\.txt|.*\.py')

for folder_name, subfolders, filenames in os.walk(folder):

    for filename in filenames: # firts.txt
       if pattern.match(filename):
           src = Path(folder_name) / filename
           dst = selected / filename
           shutil.move(src, dst)
