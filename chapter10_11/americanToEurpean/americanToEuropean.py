import re, os, shutil
from pathlib import Path

folder = Path.cwd()
home = Path.home()
(home / 'dates' ).mkdir(exist_ok=True)

pattern = re.compile(r'(.*)(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-([1-2]\d{3})(.*)')

for foldername, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        if pattern.match(filename):

            new_name = pattern.sub(r'\1\3-\2-\4\5', filename)
            shutil.move(Path(foldername) / filename, home / 'dates' / new_name)

print('Done.')

