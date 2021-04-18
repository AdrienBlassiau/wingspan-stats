import os

from definitions import OUTSIDE_ROOT_DIR, INSIDE_ROOT_DIR
from src.utils import Utils


class Path:
    """
    This class stores all the path.
    """
    DEFAULT_INPUT_PATH = OUTSIDE_ROOT_DIR + "/input/"
    DEFAULT_OUTPUT_PATH = OUTSIDE_ROOT_DIR + "/output/"
    DEFAULT_DATA_PATH = INSIDE_ROOT_DIR + "/data/"
    DEFAULT_DIST_PATH = OUTSIDE_ROOT_DIR + "/dist/"
    DEFAULT_IMAGE_PATH = INSIDE_ROOT_DIR + "/data/img/"
    DEFAULT_DIST_IMAGE_PATH = OUTSIDE_ROOT_DIR + "/dist/img/"
    DEFAULT_INI_PATH = OUTSIDE_ROOT_DIR + "/"
    DEFAULT_SCORE_OUTPUT_FILE_FORMAT = "score_{player_name}.png"
    DEFAULT_SCORE_FILE = "scores.csv"
    DEFAULT_SCORE_MODEL_FILE = "scores_model.csv"
    DEFAULT_I18N_FILE = "i18n.csv"
    DEFAULT_INI_FILE = "wingspan.stats.ini"
    DEFAULT_INI_MODEL_FILE = "wingspan.stats.model.ini"
    DEFAULT_IMAGE_FILE = "example.png"
    DEFAULT_HELP_FILE = "HELP.md"

    @staticmethod
    def get_output_save_path(player_name):
        """
        This function returns the path where we write the score of player with player_name.
        :param player_name:     The name of the player.
        :return:                The path where we write the score of player_name.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_OUTPUT_PATH)
        return os.path.join(Path.DEFAULT_OUTPUT_PATH,
                            Path.DEFAULT_SCORE_OUTPUT_FILE_FORMAT.format(player_name=player_name))

    @staticmethod
    def get_score_path():
        """
        This function returns the path where we read the scores.
        :return:                The path where we read the scores.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_INPUT_PATH)
        return os.path.join(Path.DEFAULT_INPUT_PATH, Path.DEFAULT_SCORE_FILE)

    @staticmethod
    def get_score_model_path():
        """
        This function returns the path where we read the scores model file.
        :return:                The path where we read the scores model file.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_DATA_PATH)
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_SCORE_MODEL_FILE)

    @staticmethod
    def get_i18n_path():
        """
        This function returns the path where we read the translations.
        :return:                The path where we read the translations.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_DATA_PATH)
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_I18N_FILE)

    @staticmethod
    def get_img_path():
        """
        This function returns the path where the example image is stored.
        :return:                The path where the example image is stored.
        """
        return os.path.join(Path.DEFAULT_IMAGE_PATH, Path.DEFAULT_IMAGE_FILE)

    @staticmethod
    def get_dist_img_path():
        """
        This function returns the path where the example image will be stored.
        :return:                The path where the example image will be stored.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_DIST_IMAGE_PATH)
        return os.path.join(Path.DEFAULT_DIST_IMAGE_PATH, Path.DEFAULT_IMAGE_FILE)

    @staticmethod
    def get_help_path():
        """
        This function returns the path where the help file is stored.
        :return:                The path where the help file is stored.
        """
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_HELP_FILE)

    @staticmethod
    def get_dist_help_path():
        """
        This function returns the path where the help file will be stored.
        :return:                The path where the help file will be stored.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_DIST_IMAGE_PATH)
        return os.path.join(Path.DEFAULT_DIST_PATH, Path.DEFAULT_HELP_FILE)

    @staticmethod
    def get_ini_path():
        """
        This function returns the path where we read the configurations.
        :return:                The path where we read the configurations.
        """
        return os.path.join(Path.DEFAULT_INI_PATH, Path.DEFAULT_INI_FILE)

    @staticmethod
    def get_ini_model_path():
        """
        This function returns the path where we read the model configurations.
        :return:                The path where we read the model configurations.
        """
        Utils.create_folder_if_not_exist(Path.DEFAULT_DATA_PATH)
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_INI_MODEL_FILE)