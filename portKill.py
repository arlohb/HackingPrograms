#!/usr/bin/python3

import sys
import os

args=sys.argv
command = "fuser -k -n "+args[1]+" "+args[2]
print(command)
os.system(command)
