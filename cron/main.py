import urllib
import urllib2
import time
import base64
from fab import *
from fabric.api import execute


for url in ["http://k1groups.in:8000"]:
        try:
            connection = urllib.urlopen(url)
            print(connection.getcode())
            connection.close()
        except :
            execute(k1server)
          
for url in ["http://k1groups.in:5000"]:
        try:
            connection = urllib.urlopen(url)
            print(connection.getcode())
            connection.close()
        except :
            execute(winnerserver)
