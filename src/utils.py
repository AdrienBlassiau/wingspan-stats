import os.path


class Utils:

    @staticmethod
    def create_file_if_not_exist(in_file_path, out_file_path):
        file_exists = os.path.isfile(out_file_path)

        if not file_exists:
            with open(in_file_path, "r") as in_file, \
                    open(out_file_path, "w") as out_file:
                for line in in_file:
                    out_file.write(line)
