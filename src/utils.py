import os.path


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
            with open(in_file_path, "r") as in_file, \
                    open(out_file_path, "w") as out_file:
                for line in in_file:
                    out_file.write(line)
