#!/usr/bin/env python3
import subprocess
import os

os.system("ip link show")
subprocess.call("ip addr show".split(" "))

result = subprocess.run('ls -l'.split (" "))
print (result)
