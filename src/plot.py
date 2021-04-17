import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from src.path import Path


class Plot:

    @staticmethod
    def average(lst):
        return round(sum(lst) / len(lst), 2)

    @staticmethod
    def global_text(games, player, score, i18n):
        number_games_played = games.get_player_nb_games(player)
        number_games_won = games.get_player_number_wins(player)
        number_games_won_percentage = round(number_games_won/number_games_played *100, 2)
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
    def plotBar(r, bar, bar_type, bottom, color, edgeColor, width, label, linewidth, linestyles, barcolor, textposition, games, i18n):
        mean = round(np.mean(bar), 2)
        min = round(np.min(bar), 2)
        max = round(np.max(bar), 2)
        total = sum(bar)
        best = games.get_best(bar_type)
        worst = games.get_worst(bar_type)

        plt.bar(r,
                bar,
                bottom=bottom,
                color=color,
                edgecolor=edgeColor,
                width=width,
                label=label)
        # plt.hlines(mean + textposition,
        #           -1,
        #           len(bar),
        #           color=color,
        #           linewidth=linewidth,
        #           linestyles=linestyles)

        worst_string = "*" if min == worst else " ("+str(worst)+"*"+")"
        best_string = "*" if max == best else " ("+str(best)+"*"+")"

        text = "{LABEL} {MEAN_TEXT} {mean} ({MIN_TEXT} {min}{worst}, {MAX_TEXT} {max}{best}, {TOTAL} {total})". \
            format(LABEL=i18n.colonizer(label),
                   MEAN_TEXT=i18n.translator("mean", True), mean=mean,
                   MIN_TEXT=i18n.translator("min", False), min=min, worst=worst_string,
                   MAX_TEXT=i18n.translator("max", False), max=max, best=best_string,
                   TOTAL=i18n.translator("total", False), total=total)

        t = plt.text(0, textposition, text, fontsize=15, color=color, backgroundcolor='white', zorder=20)
        t.set_bbox(dict(facecolor='white', alpha=0.7))


    @staticmethod
    def plotScore(games, player_games, games_where_player, player_name, included_games, r):
        score = [pg.get_player_score(player_name) if pg.find_player(player_name) else np.nan for pg in games_where_player]
        barwon = np.ma.masked_where(games.get_won_games(player_name, included_games), r)
        barlost = np.ma.masked_where(games.get_lost_games(player_name, included_games), r)
        barmiddle = np.ma.masked_where(games.get_middle_games(player_name, included_games), r)

        plt.scatter(barwon, score, color="#449E49", zorder=10, marker="^")
        plt.scatter(barmiddle, score, color="#FAA62B", zorder=10, marker="o")
        plt.scatter(barlost, score, color="#D33233", zorder=10, marker="v")

    @staticmethod
    def plotScores(games, player_games, games_where_player, included_games, r):
        for player_name in games.get_player_list():
            Plot.plotScore(games, player_games, games_where_player, player_name, included_games, r)

    @staticmethod
    def plot(games, player_name, i18n):
        #print(player_name)
        # y-axis in bold
        rc('font', weight='bold')
        player_games = games.get_player_games(player_name)
        games_where_player = games.get_games_where_player(player_name)
        player_number_games = games.get_player_nb_games(player_name)

        # Values of each group
        birds_bar = [s.birds for s in player_games]
        bonus_cards_bar = [s.bonus_cards for s in player_games]
        end_of_round_goals_bar = [s.end_of_round_goals for s in player_games]
        eggs_bar = [s.eggs for s in player_games]
        food_on_cards_bar = [s.food_on_cards for s in player_games]
        tucked_cards_bar = [s.tucked_cards for s in player_games]
        nectars_bar = [s.nectars for s in player_games]
        score = [s.score for s in player_games]

        # Heights of bars and text position
        bars0 = None
        textposition0 = np.mean(birds_bar)
        textposition0 = 5

        bars1 = birds_bar
        textposition1 = textposition0 + np.mean(bonus_cards_bar) + 4
        textposition1 = 10

        bars2 = np.add(birds_bar, bonus_cards_bar).tolist()
        textposition2 = textposition1 + np.mean(end_of_round_goals_bar) + 4
        textposition2 = 15

        bars3 = np.add(bars2, end_of_round_goals_bar).tolist()
        textposition3 = textposition2 + np.mean(eggs_bar) + 4
        textposition3 = 20

        bars4 = np.add(bars3, eggs_bar).tolist()
        textposition4 = textposition3 + np.mean(food_on_cards_bar) + 4
        textposition4 = 25

        bars5 = np.add(bars4, food_on_cards_bar).tolist()
        textposition5 = textposition4 + np.mean(tucked_cards_bar) + 4
        textposition5 = 30

        bars6 = np.add(bars5, tucked_cards_bar).tolist()
        textposition6 = textposition5 + np.mean(nectars_bar) + 4
        textposition6 = 35

        # The position of the bars on the x-axis
        r = np.arange(0, player_number_games, 1)

        # Names of group and bar width
        included_games = [g.index for g in player_games]

        barWidth = 1
        linewidth = 2
        edgeColor = "White"
        barcolor = "Black"

        # Create birds bar
        Plot.plotBar(r, birds_bar, "birds", bars0, '#A83E43', None, barWidth, i18n.translator("birds", True), linewidth, "solid", barcolor, textposition0, games, i18n)

        # Create bonus cards bar
        Plot.plotBar(r, bonus_cards_bar, "bonus_cards", bars1, '#3D897F', edgeColor, barWidth, i18n.translator("bonus_cards", True), linewidth, "solid",
                     barcolor, textposition1, games, i18n)

        # Create end if round goals bar
        Plot.plotBar(r, end_of_round_goals_bar, "end_of_round_goals", bars2, '#57A3CF', edgeColor, barWidth, i18n.translator("end_of_round_goals", True), linewidth,
                     "solid", barcolor, textposition2, games, i18n)
        # Create eggs bar
        Plot.plotBar(r, eggs_bar, "eggs", bars3, '#E5A841', edgeColor, barWidth, i18n.translator("eggs", True), linewidth, "solid", barcolor,
                     textposition3, games, i18n)

        # Create food on cards bar
        Plot.plotBar(r, food_on_cards_bar, "food_on_cards", bars4, '#175B51', edgeColor, barWidth, i18n.translator("food_on_cards", True), linewidth, "solid",
                     barcolor, textposition4, games, i18n)

        # Create tucked cards bar
        Plot.plotBar(r, tucked_cards_bar, "tucked_cards", bars5, '#494788', edgeColor, barWidth, i18n.translator("tucked_cards", True), linewidth, "solid",
                     barcolor, textposition5, games, i18n)

        # Create nectars bars
        Plot.plotBar(r, nectars_bar, "nectars", bars6, '#BD42A2', edgeColor, barWidth, i18n.translator("nectars", True), linewidth, "solid", barcolor,
                     textposition6, games, i18n)

        # Create win/loss/medium bar

        Plot.plotScores(games, player_games, games_where_player, included_games, r)


        # Custom X axis
        plt.xticks(r, included_games, fontweight='bold')
        plt.xlabel("Numéro de la partie")

        # Custom Y axis
        plt.ylabel("Nombre de points")

        # Legend
        #plt.legend(loc='upper right').set_zorder(20)
        plt.title('La Fiche du Petit Wingspaner : ' + player_name.capitalize())

        # Global text
        Plot.global_text(games, player_name, score, i18n)

        # Show graphic
        fig = plt.gcf()
        fig.set_size_inches((22, 11), forward=False)
        output_path = Path.get_output_save_path(player_name)
        plt.savefig(output_path, dpi=500)
        # plt.show()
        plt.clf()
