import os

from setuptools import setup

mydir = os.path.dirname(__file__)
if mydir:
    os.chdir(mydir)

setup(name = 'termcolors',
      version = '0.1',
      description = 'RGB queries on xterm-like terminals',
      packages = ['termcolors'],
      scripts = ['termcolors-demo.py']
     )
