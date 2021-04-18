# wingspan-stats
*A tool for Wingspan enthusiasts. It plot your games scores with a lot of useful informations.*

## Presentation
The tool is made to be really *user-friendly*. Two steps : 
- **First**, write all your score on the **scores.csv** file which is inside the input older,
- **Then**, create a beautiful resume of all you games by running the wingspan-stats script.

The output will look like this :

![Alt text](./img/example.png?raw=true "Title")

## Q&A section 

### How to write your score ?
Its really simple ! Open the scores.csv (inside the input folder) in your favorite csv editor (EXCEL, LibreOffice Calc, ...) and then write all
your score. It works like this : 
- **number** : is the number of the game,
- **player_name** : is the name of the player involve in the "number" game,
- **birds** : is the number of birds points of "player_name" involve in the "number" game,
- **bonus_cards** : is the number of bonus cards points of "player_name" involve in the "number" game,
- **end_of_round_goals** : is the number of end of round goals points of "player_name" involve in the "number" game,
- **eggs** : is the number of eggs points of "player_name" involve in the "number" game,
- **food_on_cards** : is the number of food on cards points of "player_name" involve in the "number" game,
- **tucked_cards** : is the number of tucked cards points of "player_name" involve in the "number" game,
- **nectars** : is the number of nectars points of "player_name" involve in the "number" game,
- **game_type** : is the type of the game (put 0 or 1 here, this feature is not used for the moment ....).

An example with three games with player A, B and C is given on player.csv file inside the archive.

### How to run the script that draw my results ?
Easy. Double click on wingspan-stats.exe (or wingspan-stats if you are on linux) ... and enjoy your performance.

### Can I customize the graph ?
Yes you can ;) It's inside the wingspan.stats.ini file. For the moment, you can : 
- **change the language** (english and french supported),
- **change the color** of the bars (in hexadecimal format).

This feature will evolve in the future !

### Any suggestion, any issue ?
You can send an email to *adblassiau@gmail.com* or create a new issue on github ;)

I will do my best to help you !