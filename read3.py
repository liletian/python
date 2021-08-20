import mmap
import contextlib

with open('file.txt', 'r') as fd:
    with contextlib.closing(mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)) as mm:
        print mm[10:]
