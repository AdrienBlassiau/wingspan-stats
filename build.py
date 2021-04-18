import PyInstaller.__main__
import os
from src.path import Path
from src.utils import Utils

"""
 In this file, we build the porject.
"""


def build():
    command = []

    # File to build
    command.append('--onefile')
    command.append('--windowed')
    command.append('--name=wingspan-stats')
    command.append('wingspan-stats.spec')

    # We create the executable file.
    PyInstaller.__main__.run(command)

    # We copy the img folder and file
    Utils.create_file_if_not_exist(Path.get_img_path(), Path.get_dist_img_path())

    # We copy the help file
    Utils.create_file_if_not_exist(Path.get_help_path(), Path.get_dist_help_path())

    # We run the app a first time to create input and input folder with example inside and also ini file.
    os.system('./wingspan-stats')

if __name__ == '__main__':
    build()
