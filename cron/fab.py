from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.network import ssh
import urllib2
import base64
env.hosts = ['root@139.162.42.125']
env.password = 'manasbhai9009'
ssh.util.log_to_file("paramiko.log", 10)


def k1server():
    env.rdir = "/home/thiru/k1groups/k118062016/"
    with cd('/home/thiru/k1groups/k118062016/'):
        run('python manage.py runserver k1groups.in:8000') 
    

def winnerserver():
    env.rdir = "/home/thiru/k1groups/k118062016/"
    with cd('/home/thiru/k1groups/k118062016/'):
        run('python manage.py runserver k1groups.in:5000') 
