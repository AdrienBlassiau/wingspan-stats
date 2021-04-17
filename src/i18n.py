import csv

from src.path import Path


class I18n:
    """
    This class reads the i18n files and manages i18n string with a dict.
    """
    def __init__(self, language):
        self.i18n_dict = {}
        self.language = language # The selected language.
        self.read_i18n_file()

    def read_i18n_file(self):
        """
        This function reads the files of translations and build a dictionary that stores all this data.
        :return:    nothing.
        """
        i18n_path = Path.get_i18n_path()
        language_list = []
        with open(i18n_path, newline='') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            row_count = 0
            for row in csvReader:
                if row_count == 0:
                    language_list = row[1:]
                elif row_count > 0:
                    self.i18n_dict[row[0]] = {}
                    for i in range(0, len(language_list)):
                        self.i18n_dict[row[0]][language_list[i]] = row[i + 1]
                row_count += 1

    def translator(self, key, capitalize=False):
        """
        This funtion translates a word to the selected language.
        :param key:         The key of the word we want to translate.
        :param capitalize:  If we want to capitalize our word.
        :return:            THe translation of the word associated to key.
        """
        selected_translation = self.i18n_dict[key][self.language]
        return selected_translation.capitalize() if capitalize else selected_translation

    def colonizer(self, text):
        """
        This function formats columns according to language convention.
        :param text:    The text where we want to add a coluln.
        :return:        The text with a column.
        """
        return text + " : " if self.language == "french" else text + ": "
