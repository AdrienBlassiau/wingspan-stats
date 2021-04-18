import shutil

import PyInstaller.__main__
import os
from src.path import Path
from src.utils import Utils

"""
 In this file, we build the project.
"""


def make_archive():
    """
    This function makes an archive of the built project.
    :return:    nothing.
    """
    Utils.delete_if_exist(Path.get_zip_path(True))
    shutil.make_archive(Path.get_zip_path(), 'zip', Utils.reverse_path_if_windows(Path.get_dist_path()))


def make_build():
    """
    This function create a build of the project.
    :return:
    """
    command = ['--onefile', '--windowed', '--name=wingspan-stats', 'wingspan-stats.spec']

    # File to build

    # We create the executable file.
    PyInstaller.__main__.run(command)

    # We copy the img folder and file
    Utils.create_file_if_not_exist(Path.get_img_path(), Path.get_dist_img_path())

    # We copy the help file
    Utils.create_file_if_not_exist(Path.get_help_path(), Path.get_dist_help_path())

    # We run the app a first time to create input and input folder with example inside and also ini file.
    os.system(Path.get_exe_path())


if __name__ == '__main__':
    make_build()
    make_archive()
