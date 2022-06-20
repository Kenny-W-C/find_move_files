'''
from os.path import isfile, join

path = "B:\\Kenny's Files\\"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)
'''
import glob
import os
import shutil

root = "B:\\Kenny's Files\\Kenny's Downloads\\"
dst_folder = "B:\\Kenny's Files\\Kenny's Docs\\Adobe\\"

count = 0
moved = 0
for filename in glob.iglob(root + '**/**', recursive=True):
    file_name = os.path.basename(filename)
    if file_name.endswith(".pdf"):
        shutil.move(filename, os.path.join(dst_folder + file_name))
        moved += 1
    count += 1
    print(filename)
    print(str(count) + ' files found. ' + str(moved) + ' files moved.')