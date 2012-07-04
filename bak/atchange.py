#! /usr/bin/env python
import sys, os.path, time, os

changedict = {}
for filename in sys.argv[1:-1]:
    changedict[filename] = os.path.getmtime(filename)

cmd = sys.argv[-1]

while 1:
    changed = False
    for filename, t in changedict.items():
        mt = os.path.getmtime(filename)
        if t != mt:
            changedict[filename] = mt
            changed = True

    if changed:
        print 'CHANGE DETECTED'
        os.system(cmd)
        continue

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
    
