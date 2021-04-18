import os
import sys

"""
Some path managment here.
"""

if getattr(sys, 'frozen', False):
    INSIDE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTSIDE_ROOT_DIR = os.path.dirname(sys.executable)
elif __file__:
    INSIDE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTSIDE_ROOT_DIR = INSIDE_ROOT_DIR
