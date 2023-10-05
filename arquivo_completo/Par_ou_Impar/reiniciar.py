import sys
import os

def restart_programa():
    python = sys.executable
    os.execl(python, python, *sys.argv)