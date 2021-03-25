import os
import shutil
import sys

dir = os.getcwd()

files = os.listdir(dir)
for sample in files:
    i = 1
    j = 1
    k = 1
    g = 1
    fnam = os.path.basename(sample.split('_')[0]).format(i)
    fnams = os.path.basename(sample.split('_')[0]).format(j)

    fsp = os.path.basename(sample.split('_')[0]).format(i)
    fsps = os.path.basename(sample.split('_')[0]).format(j)

    ftomove = os.path.basename(sample).format(k)
    while not os.path.exists(fnam):
        os.mkdir(fnam)
        i += 1

    if os.path.exists(fnam) and fnam == fnams:
        if os.path.exists(fsp) and fsp == fsps:
            shutil.move(ftomove, fnam)
            j += 1
            k += 1
            g += 1