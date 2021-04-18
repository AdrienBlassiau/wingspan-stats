import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from src.path import Path


class Plot:
    """
    This class plots the scores a player.
    """

    @staticmethod
    def global_text(games, player, score, i18n):
        """
        This function prints the text in the top of the file.
        :param games:   The games played.
        :param player:  The player concerned by the current plot.
        :param score:   The score of the player.
        :param i18n:    A translation module.
        :return:        nothing.
        """
        number_games_played = games.get_player_nb_games(player)
        number_games_won = games.get_player_number_wins(player)
        number_games_won_percentage = round(number_games_won / number_games_played * 100, 2)
        number_games_lost = games.get_player_number_loses(player)
        number_games_lost_percentage = round(number_games_lost / number_games_played * 100, 2)

        mean = round(np.mean(score), 2)
        min = round(np.min(score), 2)
        max = round(np.max(score), 2)
        best = games.get_best("score")
        worst = games.get_worst("score")
        worst_string = "*" if min == worst else " (" + str(worst) + "*" + ")"
        best_string = "*" if max == best else " (" + str(best) + "*" + ")"

        score_resume = "{MEAN_SCORE} {mean} ({WORST_SCORE} {min}{worst}, {BEST_SCORE} {max}{best})". \
            format(MEAN_SCORE=i18n.translator("mean_score", True),
                   mean=mean,
                   WORST_SCORE=i18n.translator("worst_score", True),
                   min=min,
                   worst=worst_string,
                   BEST_SCORE=i18n.translator("best_score", True),
                   max=max,
                   best=best_string)

        text = "{NUMBER_GAMES_PLAYED} {number_games_played} \n " \
               "{NUMBER_GAMES_WON_LOST} " \
               "{number_games_won} ({number_games_won_percentage}%)/" \
               "{number_games_lost} ({number_games_lost_percentage}%) \n" \
               "{score_resume} \n" \
            .format(NUMBER_GAMES_PLAYED=i18n.translator("games_played", True),
                    number_games_played=number_games_played,
                    NUMBER_GAMES_WON_LOST=i18n.translator("games_won_lost", True),
                    number_games_won=number_games_won,
                    number_games_won_percentage=number_games_won_percentage,
                    number_games_lost=number_games_lost,
                    number_games_lost_percentage=number_games_lost_percentage,
                    score_resume=score_resume)
        ax = plt.gca()
        plt.text(0.5,
                 0.93,
                 text,
                 fontsize=15,
                 color="black",
                 ha='center',
                 va='center',
                 transform=ax.transAxes)

    @staticmethod
    def plotBar(r, bar, source_of_points, bottom, colors, edgeColor, width, linewidth, linestyles, barcolor,
                textposition,
                games, i18n):
        """
        This function prints information about a given source of points.
        :param r:                The game played.
        :param bar:              The data related to the given source of point for each game.
        :param source_of_points: The source of points concerned by this bar.
        :param bottom:           The bottom position of the bar.
        :param colors:           The color manager.
        :param edgeColor:        The edge colors of the bar.
        :param width:            The width of the bar.
        :param linewidth:        The line width of the bar (not used).
        :param linestyles:       The line style of the bar (not used).
        :param barcolor:         The color of the bar (not used).
        :param textposition:     The position of the text.
        :param games:            The games object.
        :param i18n:             THe translation module.
        :return:
        """

        # We compute some data
        mean = round(np.mean(bar), 2)
        min = round(np.min(bar), 2)
        max = round(np.max(bar), 2)
        total = sum(bar)
        best = games.get_best(source_of_points)
        worst = games.get_worst(source_of_points)
        source_of_point_string = i18n.translator(source_of_points, True)
        color_string = colors.get_color(source_of_points)

        # We plot a bar for the concerned source of point
        plt.bar(r,
                bar,
                bottom=bottom,
                color=color_string,
                edgecolor=edgeColor,
                width=width,
                label=source_of_point_string)

        # We add some information about the concerned source of point.
        worst_string = "*" if min == worst else " (" + str(worst) + "*" + ")"
        best_string = "*" if max == best else " (" + str(best) + "*" + ")"

        text = "{LABEL} {MEAN_TEXT} {mean}, {MIN_TEXT} {min}{worst}, {MAX_TEXT} {max}{best}, {TOTAL} {total}". \
            format(LABEL=source_of_point_string+" | ",
                   MEAN_TEXT=i18n.translator("mean", False), mean=mean,
                   MIN_TEXT=i18n.translator("min", False), min=min, worst=worst_string,
                   MAX_TEXT=i18n.translator("max", False), max=max, best=best_string,
                   TOTAL=i18n.translator("total", False), total=total)

        t = plt.text(0, textposition, text, fontsize=15, color=color_string, backgroundcolor='white', zorder=20)
        t.set_bbox(dict(facecolor='white', alpha=0.7))

    @staticmethod
    def plotScore(games, games_where_player, player_name, included_games, r):
        """
        This function adds some infos on bars about other player, oncluding the current player.
        :param games:               The games object.
        :param games_where_player:  The games where the current player appears.
        :param player_name:         The name of the player.
        :param included_games:      The list of game indexes where  current player appears.
        :param r:                   A range of game played.
        :return:                    nothing.
        """
        score = [pg.get_player_score(player_name) if pg.find_player(player_name) else np.nan for pg in
                 games_where_player]
        barwon = np.ma.masked_where(games.get_won_games(player_name, included_games), r)
        barlost = np.ma.masked_where(games.get_lost_games(player_name, included_games), r)
        barmiddle = np.ma.masked_where(games.get_middle_games(player_name, included_games), r)

        plt.scatter(barwon, score, color="#449E49", zorder=10, marker="^")
        plt.scatter(barmiddle, score, color="#FAA62B", zorder=10, marker="o")
        plt.scatter(barlost, score, color="#D33233", zorder=10, marker="v")

    @staticmethod
    def plotScores(games, games_where_player, included_games, r):
        """
        This function adds some infos on bars about each player of each game.
        :param games:               The games object.
        :param games_where_player:  The games where the current player appears.
        :param included_games:      The list of game indexes where  current player appears.
        :param r:                   A range of game played.
        :return:                    nothing.
        """
        for player_name in games.get_player_list():
            Plot.plotScore(games, games_where_player, player_name, included_games, r)

    @staticmethod
    def plot(games, player_name, i18n, colors):
        """
        This functions plot the score of the game played by the player with player_name.
        :param games:       The list of games.
        :param player_name: The name of the player.
        :param i18n:        The translation module.
        :return:            nothing.
        """

        # y-axis in bold
        rc('font', weight='bold')

        # Get useful data.
        player_games = games.get_player_games(player_name)
        games_where_player = games.get_games_where_player(player_name)
        player_number_games = games.get_player_nb_games(player_name)

        # Values of each group
        birds_bar = [g.birds for g in player_games]
        bonus_cards_bar = [g.bonus_cards for g in player_games]
        end_of_round_goals_bar = [g.end_of_round_goals for g in player_games]
        eggs_bar = [g.eggs for g in player_games]
        food_on_cards_bar = [g.food_on_cards for g in player_games]
        tucked_cards_bar = [g.tucked_cards for g in player_games]
        nectars_bar = [g.nectars for g in player_games]
        score = [g.score for g in player_games]
        included_games = [g.index for g in player_games]

        # Heights of bars and text position
        bars0 = None
        text_position0 = 5

        bars1 = birds_bar
        text_position1 = 10

        bars2 = np.add(birds_bar, bonus_cards_bar).tolist()
        text_position2 = 15

        bars3 = np.add(bars2, end_of_round_goals_bar).tolist()
        text_position3 = 20

        bars4 = np.add(bars3, eggs_bar).tolist()
        text_position4 = 25

        bars5 = np.add(bars4, food_on_cards_bar).tolist()
        text_position5 = 30

        bars6 = np.add(bars5, tucked_cards_bar).tolist()
        text_position6 = 35

        # The position of the bars on the x-axis
        r = np.arange(0, player_number_games, 1)

        barWidth = 1
        linewidth = 2
        edgeColor = "White"
        barcolor = "Black"

        # Create birds bar
        Plot.plotBar(r, birds_bar, "birds", bars0, colors, None, barWidth, linewidth,
                     "solid", barcolor, text_position0, games, i18n)

        # Create bonus cards bar
        Plot.plotBar(r, bonus_cards_bar, "bonus_cards", bars1, colors, edgeColor, barWidth, linewidth, "solid",
                     barcolor, text_position1, games, i18n)

        # Create end if round goals bar
        Plot.plotBar(r, end_of_round_goals_bar, "end_of_round_goals", bars2, colors, edgeColor, barWidth, linewidth,
                     "solid", barcolor, text_position2, games, i18n)
        # Create eggs bar
        Plot.plotBar(r, eggs_bar, "eggs", bars3, colors, edgeColor, barWidth, linewidth,
                     "solid", barcolor,
                     text_position3, games, i18n)

        # Create food on cards bar
        Plot.plotBar(r, food_on_cards_bar, "food_on_cards", bars4, colors, edgeColor, barWidth, linewidth, "solid",
                     barcolor, text_position4, games, i18n)

        # Create tucked cards bar
        Plot.plotBar(r, tucked_cards_bar, "tucked_cards", bars5, colors, edgeColor, barWidth, linewidth, "solid",
                     barcolor, text_position5, games, i18n)

        # Create nectars bars
        Plot.plotBar(r, nectars_bar, "nectars", bars6, colors, edgeColor, barWidth,
                     linewidth, "solid", barcolor,
                     text_position6, games, i18n)

        # Create win/loss/medium bar
        Plot.plotScores(games, games_where_player, included_games, r)

        # Custom X axis
        plt.xticks(r, included_games, fontweight='bold')
        plt.xlabel(i18n.translator('index_of_game', True))

        # Custom Y axis
        plt.ylabel(i18n.translator('number_of_points', True))

        # Legend
        # plt.legend(loc='upper right').set_zorder(20)

        # Title
        plt.title(i18n.translator('the_little_wingspaner_sheet', True) + ' ' + player_name.capitalize())

        # Global text
        Plot.global_text(games, player_name, score, i18n)

        # Show graphic
        fig = plt.gcf()
        fig.set_size_inches((22, 11), forward=False)
        plt.savefig(Path.get_output_save_path(player_name), dpi=500)
        plt.clf()
