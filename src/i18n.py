import csv

from src.path import Path


class I18n:

    def __init__(self, language):
        self.i18n_dict = {}
        self.language = language
        self.read_i18n_file()

    def read_i18n_file(self):
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
        selected_translation = self.i18n_dict[key][self.language]
        return selected_translation.capitalize() if capitalize else selected_translation

    def colonizer(self, text):
        return text + " : " if self.language == "french" else text + ": "
