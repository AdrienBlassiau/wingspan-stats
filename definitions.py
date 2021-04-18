import os
import sys

# determine if application is a script file or frozen exe

if getattr(sys, 'frozen', False):
    INSIDE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTSIDE_ROOT_DIR = os.path.dirname(sys.executable)
elif __file__:
    INSIDE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTSIDE_ROOT_DIR = INSIDE_ROOT_DIR

print(INSIDE_ROOT_DIR, OUTSIDE_ROOT_DIR)