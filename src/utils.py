import errno
import os.path
import shutil

class Utils:
    """
    This class stores some useful functions
    """

    @staticmethod
    def create_file_if_not_exist(in_file_path, out_file_path):
        """
        This file writes the content of an input file into an output file.
        :param in_file_path:    The input file path.
        :param out_file_path:   The output file path.
        :return:                nothing.
        """
        file_exists = os.path.isfile(out_file_path)

        if not file_exists:
            with open(in_file_path, "r"), \
                    open(out_file_path, "w"):
                shutil.copyfile(in_file_path, out_file_path)

    @staticmethod
    def create_folder_if_not_exist(folder_path):
        if not os.path.exists(os.path.dirname(folder_path)):
            try:
                os.makedirs(os.path.dirname(folder_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
