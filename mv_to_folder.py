import os
import shutil

dir = 'path to fasta/files'

files = os.listdir(dir)
for sample in files:
    i = 1
    j = 1
    k = 1
    g = 1
    fnam = os.path.basename(sample[0:12]).format(i)
    fnams = os.path.basename(sample[0:12]).format(j)
    ftomove = os.path.basename(sample).format(k)
    while not os.path.exists(fnam):
        os.mkdir(fnam)
        i += 1

    if os.path.exists(fnam) and fnam == fnams :
        shutil.move(ftomove,fnam).format(g)
        j += 1
        k += 1
        g += 1



