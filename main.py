from src.games import Games
from src.log import Log

import logging


def main():
    """
    Main function, run configuration then score import and finally plot data.
    :return:    nothing.
    """
    games = Games()
    games.run_config()
    games.run_import()
    games.run_plot()


if __name__ == '__main__':
    Log.setup()
    logging.info('Start generation ...')
    main()
    logging.info('Finished with success !')
