from src.games import Games


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
    main()
