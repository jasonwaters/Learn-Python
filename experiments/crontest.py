#!/usr/bin/env python
import sys, os
from datetime import datetime, date, time

homedir = os.path.expanduser("~")

log = open(homedir + '/Desktop/cronlog.txt','a')

if len(sys.argv) >1:
    log.write(sys.argv[1]+' '+str(datetime.now())+'\n')
else:
    log.write(str(datetime.now())+'\n')

log.close()
