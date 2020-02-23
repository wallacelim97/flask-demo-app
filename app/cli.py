import os
import click
from app import app

@app.cli.group()
def setup():
    """ Commands for setting up this project """
    pass

@setup.command()
def init():
    """ Resolve [ -d "YOUR_DIR" ] && echo "is a dir" and run """        
    os.system('echo create macros at \'app/cli.py\'')
    