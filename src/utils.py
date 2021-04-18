import errno
import os
import os.path
import shutil
import platform


class Utils:
    """
    This class stores some useful functions
    """

    @staticmethod
    def delete_if_exist(file_path):
        """
        This function deletes a file if it exists.
        :param file_path:   The file we want to delete.
        :return:            nothing.
        """
        import os
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def create_file_if_not_exist(in_file_path, out_file_path):
        """
        This funtion writes the content of an input file into an output file.
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
        """
        This function create a folder if doesn't exist.
        :param folder_path:     The name of the folder we want to create.
        :return:                nothing.
        """
        if not os.path.exists(os.path.dirname(folder_path)):
            try:
                os.makedirs(os.path.dirname(folder_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    @staticmethod
    def is_linux():
        """
        THis function test if we are using linux.
        :return:    True if we are using linux.
        """
        return platform.system() == 'Linux'

    @staticmethod
    def is_windows():
        """
        THis function test if we are using windows.
        :return:    True if we are using windows.
        """
        return platform.system() == 'Windows'

    @staticmethod
    def is_mac():
        """
        THis function test if we are using mac.
        :return:    True if we are using mac.
        """
        return platform.system() == 'Darwin'

    @staticmethod
    def reverse_path_if_windows(path):
        path.replace('\\', '/') if Utils.is_windows() else path
